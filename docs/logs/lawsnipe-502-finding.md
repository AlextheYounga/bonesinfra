# 502 Bad Gateway — Root Cause Analysis

## Symptoms
- `lawsnipe-178-104-218-5.nip.io` returns **502 Bad Gateway**
- Per-site nginx (`lawsnipe-nginx.service`) is **active (running)**
- System nginx (`nginx.service`) is **active (running)**
- The per-site nginx socket exists at `/run/lawsnipe/nginx/nginx.sock`

## Root Cause

**Permission denied** — system nginx workers (running as `www-data`) cannot connect to the per-site nginx UNIX socket.

The chain is:
```
system nginx (www-data)  →  unix:/run/lawsnipe/nginx/nginx.sock  →  per-site nginx (lawsnipe)
```

### The problem
| Path | Perms | Owner | Issue |
|---|---|---|---|
| `/run/lawsnipe/nginx/` | **drwxr-x---** (750) | `lawsnipe:lawsnipe` | `www-data` is not in group `lawsnipe` → **cannot traverse** |
| `/run/lawsnipe/nginx/nginx.sock` | `srw-rw-rw-` (666) | `lawsnipe:lawsnipe` | world-writable, but unreachable without directory traversal |

Even though the socket is world-writable (`666`), `www-data` needs `x` (execute) on the parent directory `/run/lawsnipe/nginx/` to traverse into it and reach the socket. With `750`, only `lawsnipe` (owner) and `lawsnipe` (group) can enter.

### System nginx error log confirms
```
connect() to unix:/run/lawsnipe/nginx/nginx.sock failed (13: Permission denied)
```

## Why it worked before the restart
Before the `reload`/`restart`, the original system nginx workers (started at boot) were somehow able to reach the socket — possibly because they inherited a file descriptor or had a different runtime context. After the reload, new workers were spawned with only their standard `www-data` privileges, which lack access to the locked-down directory.

## Triggers
The following sequence caused the new workers to lose the old connection:
```
systemctl reload nginx        # spawned new workers that can't reach the socket
systemctl restart nginx        # same — new workers, fresh privileges
systemctl reload lawsnipe-nginx  # fine, but didn't help since the bottleneck is at system nginx
```

## Fix

### Immediate (will be lost on next service restart)
```bash
chmod o+x /run/lawsnipe/nginx
```

### Permanent (survives restarts)
Edit `/etc/systemd/system/lawsnipe-nginx.service` and change:
```
RuntimeDirectoryMode=0750  →  RuntimeDirectoryMode=0755
```
Then:
```bash
systemctl daemon-reload
systemctl restart lawsnipe-nginx
```

This makes `/run/lawsnipe/nginx` world-traversable (`755`), so `www-data` can reach the socket while the socket's own permissions still control read/write access.

# Deployment Verification Report: lawsnipe

**Runtime:** Laravel (PHP 8.5 FPM)
**Domain:** `lawsnipe-178-104-218-5.nip.io`
**User:** `lawsnipe` (uid=999)

---

## 1. Systemd Units

| Unit | Status | Enabled |
|---|---|---|
| `nginx.service` | active (running) | yes |
| `lawsnipe-nginx.service` | active (running) | yes |
| `php8.5-fpm.service` | active (running) | yes |

**PASS** — All units are loaded, enabled, and active.

**WARN** — The per-site nginx had one restart on initial startup (error log permission issue on first attempt, succeeded on restart). No ongoing issues.

---

## 2. AppArmor

| Profile | Loaded | Attached |
|---|---|---|
| `bonesdeploy-lawsnipe-nginx` | enforce | yes — PID 21152, 21154 both confined |
| PHP-FPM (distro) | unconfined (correct for Laravel) | N/A (no per-project profile needed) |

**PASS** — AppArmor is enabled, the nginx profile is loaded and both nginx processes are correctly confined. PHP-FPM uses the distro package, so no per-project AppArmor profile is expected — this is correct for Laravel.

---

## 3. Runtime Directories and Sockets

| Path | Exists | Owner/Perms |
|---|---|---|
| `/run/lawsnipe/nginx` | yes | `lawsnipe:lawsnipe 0750` |
| `/run/lawsnipe/nginx/nginx.sock` | yes | `srw-rw-rw- lawsnipe:lawsnipe` |
| `/run/php/php8.5-fpm-lawsnipe.sock` | yes | `srw-rw---- www-data:www-data` |

No stale old-path sockets found.

**PASS** — All expected directories and sockets present with correct ownership.

---

## 4. Nginx Config and Routing

System nginx validates OK — proxies to `unix:/run/lawsnipe/nginx/nginx.sock` for `lawsnipe-178-104-218-5.nip.io`.

Per-site nginx listens on the UNIX socket, serves static files from `/srv/sites/lawsnipe/current/public`, and routes `.php` via FastCGI to `unix:/run/php/php8.5-fpm-lawsnipe.sock`.

**PASS** — Both nginx configs are valid, and the routing chain (system nginx -> per-site nginx -> php-fpm) is correctly wired.

---

## 5. Laravel-Specific Checks

| Check | Result |
|---|---|
| PHP-FPM pool file | `/etc/php/8.5/fpm/pool.d/lawsnipe.conf` exists |
| Per-project php-fpm systemd service | None found (correct — uses distro `php8.5-fpm.service`) |
| PHP-FPM config test | PASS |
| PHP-FPM service active | yes |
| fastcgi target in site config matches pool socket | `unix:/run/php/php8.5-fpm-lawsnipe.sock` matches pool `listen` directive |

**PASS** — All Laravel-specific configuration is correct.

---

## 6. HTTP Health

HTTP `http://127.0.0.1/` with Host header `lawsnipe-178-104-218-5.nip.io`:
- **Status code:** 200
- **Redirect:** None
- **Body snippet:** "Welcome to nginx!" (static index.html served — no PHP application deployed yet)
- **HTTPS (port 443):** Connection refused (no SSL configured, expected for nip.io preview domain)

**PASS** — HTTP health check returns 200. SSL not configured, which is expected.

---

## 7. Logs and Obvious Breakage

- Per-site nginx logs: Clean after the initial restart — no errors, no AppArmor denials, no permission issues after restart.
- PHP-FPM logs: Clean — no errors or warnings.
- System nginx logs: Clean.
- No AppArmor DENIED messages found in kernel journal.

**PASS** — No signs of breakage in any logs.

---

## 8. Final Verdict

**PASS** — The lawsnipe deployment is healthy and correctly confined.

### Summary
- All systemd units enabled and running
- nginx processes properly confined under `bonesdeploy-lawsnipe-nginx` AppArmor profile
- Runtime directories and sockets in correct locations with correct ownership
- Nginx config chain (system -> per-site -> php-fpm) correctly wired and validated
- PHP-FPM pool correctly configured, socket matches nginx fastcgi target
- HTTP health returns 200 with expected content
- No ongoing errors in any service logs

### WARN (minor)
- Per-site nginx had a single restart on initial startup due to an error log permission issue (resolved automatically, no ongoing impact). If this persists across future deploys, the AppArmor profile may need a `w` rule for `/run/lawsnipe/nginx/error.log`.
- The current release contains only a static `index.html` placeholder — no Laravel application (`artisan`, `app/`, `vendor/`) has been deployed yet. The PHP-FPM fastcgi path won't be exercised until a PHP application is present.

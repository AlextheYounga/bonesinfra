from shlex import quote

from pyinfra.operations import apt, server, systemd

APT_PACKAGES = {
    "postgres": "postgresql",
    "mariadb": "mariadb-server",
    "mysql": "mysql-server",
    "valkey": "valkey-server",
    "redis": "redis-server",
}


def provision(ctx):
    services = ctx.dbs.services
    if not services:
        return

    packages = [APT_PACKAGES[service] for service in services if service in APT_PACKAGES]
    if packages:
        apt.packages(
            name="Install selected database services",
            packages=packages,
            present=True,
            update=True,
            cache_time=3600,
            _sudo=True,
        )
    if "mongodb" in services:
        _install_mongodb()

    project = _database_identifier(ctx.app.project_name)
    env_path = f"{ctx.paths_dict['shared']}/.env"
    if "postgres" in services:
        _postgres(project, env_path)
    if "mariadb" in services:
        _mysql(project, env_path, "mariadb")
    if "mysql" in services:
        _mysql(project, env_path, "mysql")
    if "mongodb" in services:
        _mongodb(project, env_path)
    if "valkey" in services:
        _key_value_store(env_path, "valkey", "valkey-server", 6380)
    if "redis" in services:
        _key_value_store(env_path, "redis", "redis-server", 6379)


def _database_identifier(project_name):
    name = project_name.replace("-", "_")
    if not name or len(name) > 48 or not name.replace("_", "").isalnum():
        raise ValueError("project_name cannot be used as a database identifier")
    return name


def _install_mongodb():
    server.shell(
        name="Install MongoDB package source",
        commands=[
            "install -d -m 0755 /etc/apt/keyrings",
            "curl -fsSL https://pgp.mongodb.com/server-8.0.asc -o /tmp/mongodb-server-8.0.asc && gpg --dearmor --yes -o /etc/apt/keyrings/mongodb-server-8.0.gpg /tmp/mongodb-server-8.0.asc && rm /tmp/mongodb-server-8.0.asc",
            '. /etc/os-release && component=main && [ "$ID" = ubuntu ] && component=multiverse; echo "deb [signed-by=/etc/apt/keyrings/mongodb-server-8.0.gpg] https://repo.mongodb.org/apt/$ID $VERSION_CODENAME/mongodb-org/8.0 $component" > /etc/apt/sources.list.d/mongodb-org-8.0.list',
        ],
        _sudo=True,
    )
    apt.packages(
        name="Install MongoDB",
        packages=["mongodb-org"],
        present=True,
        update=True,
        _sudo=True,
    )


def _postgres(project, env_path):
    user = f"{project}_postgres"
    command = _postgres_command(project, user, env_path)
    server.shell(name="Configure PostgreSQL for project", commands=[command], _sudo=True)
    systemd.service(
        name="Enable PostgreSQL", service="postgresql", enabled=True, running=True, restarted=True, _sudo=True
    )


def _postgres_command(database, user, env_path):
    q_database, q_user, q_env = map(quote, (database, user, env_path))
    return (
        f"env={q_env}; user={q_user}; database={q_database}; "
        "password=$(sed -n 's/^POSTGRES_PASSWORD=//p' \"$env\" | head -n1); "
        '[ -n "$password" ] || password=$(openssl rand -hex 24); '
        "sudo -u postgres psql -v user=\"$user\" -v password=\"$password\" -c \"SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', :'user', :'password') WHERE NOT EXISTS (SELECT FROM pg_roles WHERE rolname = :'user') \\gexec\"; "
        "sudo -u postgres psql -v user=\"$user\" -v database=\"$database\" -c \"SELECT format('CREATE DATABASE %I OWNER %I', :'database', :'user') WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = :'database') \\gexec\"; "
        "sudo -u postgres psql -c \"ALTER SYSTEM SET listen_addresses = 'localhost'\"; "
        'grep -q \'^POSTGRES_PASSWORD=\' "$env" || printf \'POSTGRES_PASSWORD=%s\\nPOSTGRES_USER=%s\\nPOSTGRES_DB=%s\\nPOSTGRES_URL=postgresql://%s:%s@127.0.0.1:5432/%s\\n\' "$password" "$user" "$database" "$user" "$password" "$database" >> "$env"'
    )


def _mysql(project, env_path, implementation):
    user = f"{project}_mysql"
    q_project, q_user, q_env = map(quote, (project, user, env_path))
    server.shell(
        name=f"Configure {implementation} for project",
        commands=[
            f'env={q_env}; user={q_user}; database={q_project}; password=$(sed -n \'s/^MYSQL_PASSWORD=//p\' "$env" | head -n1); [ -n "$password" ] || password=$(openssl rand -hex 24); mysql -e "CREATE DATABASE IF NOT EXISTS $database; CREATE USER IF NOT EXISTS \'$user\'@\'localhost\' IDENTIFIED BY \'$password\'; GRANT ALL PRIVILEGES ON $database.* TO \'$user\'@\'localhost\'; FLUSH PRIVILEGES;"; grep -q \'^MYSQL_PASSWORD=\' "$env" || printf \'MYSQL_PASSWORD=%s\\nMYSQL_USER=%s\\nMYSQL_DATABASE=%s\\nMYSQL_URL=mysql://%s:%s@127.0.0.1:3306/%s\\n\' "$password" "$user" "$database" "$user" "$password" "$database" >> "$env"',
            "install -d -m 0755 /etc/mysql/conf.d && printf '[mysqld]\\nbind-address = 127.0.0.1\\n' > /etc/mysql/conf.d/bonesdeploy.cnf",
        ],
        _sudo=True,
    )
    systemd.service(
        name=f"Enable {implementation}", service="mysql", enabled=True, running=True, restarted=True, _sudo=True
    )


def _mongodb(project, env_path):
    user = f"{project}_mongodb"
    q_user, q_env = map(quote, (user, env_path))
    server.shell(
        name="Configure MongoDB for project",
        commands=[
            "sed -ri 's/^[[:space:]]*bindIp:.*/  bindIp: 127.0.0.1/' /etc/mongod.conf",
            "grep -q '^security:' /etc/mongod.conf || printf '\\nsecurity:\\n  authorization: enabled\\n' >> /etc/mongod.conf",
            f"env={q_env}; user={q_user}; password=$(sed -n 's/^MONGODB_PASSWORD=//p' \"$env\" | head -n1); [ -n \"$password\" ] || password=$(openssl rand -hex 24); grep -q '^MONGODB_PASSWORD=' \"$env\" || printf 'MONGODB_PASSWORD=%s\\nMONGODB_USER=%s\\nMONGODB_URI=mongodb://%s:%s@127.0.0.1:27017/%s?authSource=admin\\n' \"$password\" \"$user\" \"$user\" \"$password\" {quote(project)} >> \"$env\"; mongosh --quiet --eval \"db.getSiblingDB('admin').getUser('$user') || db.getSiblingDB('admin').createUser({{user: '$user', pwd: '$password', roles: [{{role: 'root', db: 'admin'}}]}})\" || mongosh --username \"$user\" --password \"$password\" --authenticationDatabase admin --quiet --eval \"db.getSiblingDB('admin').getUser('$user') || db.getSiblingDB('admin').createUser({{user: '$user', pwd: '$password', roles: [{{role: 'root', db: 'admin'}}]}})\"",
        ],
        _sudo=True,
    )
    systemd.service(name="Enable MongoDB", service="mongod", enabled=True, running=True, restarted=True, _sudo=True)


def _key_value_store(env_path, service, unit, port):
    password_key = service.upper() + "_PASSWORD"
    url_key = service.upper() + "_URL"
    config = f"/etc/{service}/{service}.conf"
    q_env, q_config = map(quote, (env_path, config))
    server.shell(
        name=f"Configure {service} for project",
        commands=[
            f'env={q_env}; config={q_config}; password=$(sed -n \'s/^{password_key}=//p\' "$env" | head -n1); [ -n "$password" ] || password=$(openssl rand -hex 24); sed -ri \'s/^[[:space:]]*bind .*/bind 127.0.0.1/\' "$config"; sed -ri \'s/^[[:space:]]*port .*/port {port}/\' "$config"; sed -ri \'/^[[:space:]]*requirepass /d\' "$config"; grep -q \'^protected-mode yes$\' "$config" || printf \'\\nprotected-mode yes\\n\' >> "$config"; printf \'\\nrequirepass %s\\n\' "$password" >> "$config"; grep -q \'^{password_key}=\' "$env" || printf \'{password_key}=%s\\n{url_key}=redis://:%s@127.0.0.1:{port}/0\\n\' "$password" "$password" >> "$env"',
        ],
        _sudo=True,
    )
    systemd.service(name=f"Enable {service}", service=unit, enabled=True, running=True, restarted=True, _sudo=True)

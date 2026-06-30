from pyinfra.operations import server

CARGO_BIN = "/root/.cargo/bin/cargo"
HELPER_CARGO_CRATES: list[str] = [
    "tuimux", # https://github.com/AlextheYounga/tuimux
]

def install_helper_crates():
    for crate in HELPER_CARGO_CRATES:
        server.shell(
            name=f"Install {crate} binary",
            commands=[f"{CARGO_BIN} install {crate}"],
            _sudo=True,
        )

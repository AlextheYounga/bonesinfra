from pyinfra.operations import apt, server


# Install https://github.com/mexirica/aptui
def _add_aptui_repository():
    server.shell(
        name="Add aptui repository",
        commands=[
            "curl -fsSL https://mexirica.github.io/aptui/public-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/aptui-archive-keyring.gpg",  # noqa: E501
            "echo 'deb [signed-by=/usr/share/keyrings/aptui-archive-keyring.gpg] https://mexirica.github.io/aptui/ stable main' | sudo tee /etc/apt/sources.list.d/aptui.list",  # noqa: E501
        ],
        _sudo=True,
    )


def install_aptui():
    _add_aptui_repository()
    apt.packages(
        name="Install aptui",
        packages=["aptui"],
        update=True,
        _sudo=True,
    )

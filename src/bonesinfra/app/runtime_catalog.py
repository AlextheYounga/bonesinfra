from bonesinfra.runtimes import get_runtime, list_runtimes


def list_all() -> list[str]:
    return list_runtimes()


def get_questions(runtime_name: str) -> list[dict]:
    module = get_runtime(runtime_name)
    return module.questions()

from pathlib import Path


def getssh() -> Path:
    return Path.home().joinpath(".ssh")

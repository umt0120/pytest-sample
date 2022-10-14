from pathlib import Path


def getssh():
    return Path.home().joinpath(".ssh")
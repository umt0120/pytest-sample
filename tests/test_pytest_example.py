from pathlib import Path

import pytest
from typing import Annotated, Generator
from pytest import MonkeyPatch

from pytest_example.pytest_example import getssh


def test_needfiles(tmp_path: Path):
    """一時ディレクトリを作成する組み込みfixtureのtmp_pathの例

    Args:
        tmp_path (Path): 組み込みfixture
    """
    print(tmp_path)
    assert isinstance(tmp_path, Path)
    assert tmp_path.is_dir()
    assert tmp_path.exists()


def test_getssh(monkeypatch: MonkeyPatch):
    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)

    actual = getssh()
    assert actual == Path("/abc/.ssh")


@pytest.fixture
def yield_fixture() -> Generator[int, None, None]:
    print("before yield")
    yield 0
    print("after yield")


def test_yield_fixture(yield_fixture: Annotated[Generator[int, None, None], pytest.fixture]) -> None:
    assert yield_fixture == 0

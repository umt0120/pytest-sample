from pathlib import Path


def test_needfiles(tmp_path: Path):
    """一時ディレクトリを作成する組み込みfixtureのtmp_pathの例
    
    Args:
        tmp_path (Path): 組み込みfixture 
    """
    print(tmp_path)
    assert isinstance(tmp_path, Path)
    assert tmp_path.is_dir()
    assert tmp_path.exists()
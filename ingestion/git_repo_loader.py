# ingestion/git_repo_loader.py
import subprocess
from pathlib import Path

def clone_repo(repo_url: str, target_dir: Path):
    if target_dir.exists():
        return

    subprocess.run(
        ["git", "clone", repo_url, str(target_dir)],
        check=True,
        timeout=60
    )
"""Git repository loader module."""
# ingestion/task_file_loader.py
from pathlib import Path

def load_task_file(path: str) -> str:
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(path)

    if file.suffix != ".txt":
        raise ValueError("כרגע נתמך רק TXT")

    return file.read_text(encoding="utf-8")
"""Task file loader module."""
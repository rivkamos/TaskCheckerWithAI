# analysis/snapshot_builder.py
from pathlib import Path

MAX_FILE_SIZE = 5_000  # תווים

def build_code_snapshot(project_path: Path) -> str:
    parts = []

    for file in project_path.rglob("*.py"):
        try:
            content = file.read_text(encoding="utf-8")
            content = content[:MAX_FILE_SIZE]

            parts.append(
                f"\n# FILE: {file.relative_to(project_path)}\n{content}"
            )
        except Exception:
            continue

    return "\n".join(parts)
"""Code snapshot builder module."""
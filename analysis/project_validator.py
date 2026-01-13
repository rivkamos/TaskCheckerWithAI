# analysis/project_validator.py
import subprocess
from pathlib import Path

def validate_project(project_path: Path) -> list[str]:
    issues = []

    if not (project_path / "requirements.txt").exists():
        issues.append("חסר requirements.txt")

    try:
        subprocess.run(
            ["python", "-m", "compileall", "."],
            cwd=project_path,
            capture_output=True,
            timeout=20,
            check=True
        )
    except subprocess.CalledProcessError:
        issues.append("שגיאות תחביר בקוד")
    except subprocess.TimeoutExpired:
        issues.append("בדיקת קוד נתקעה (timeout)")

    return issues
"""Project validator module."""
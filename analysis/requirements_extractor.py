# analysis/requirements_extractor.py
import json
import re
from models.requirements import Requirement
from llm.base import LLMClient

def extract_requirements(task_text: str, llm: LLMClient) -> list[Requirement]:
    prompt = f"""
    נתח את מסמך המשימה והפק רשימת דרישות ברורה.
    החזר JSON בפורמט בלבד, ללא טקסט נוסף:
    [
      {{
        "id": "REQ-1",
        "description": "...",
        "category": "functional|technical"
      }}
    ]

    מסמך:
    {task_text}
    """

    raw = llm.complete(prompt)
    
    # Debug - ראה מה מוחזר
    print(f"DEBUG - Raw response:\n{raw}\n")
    
    # נקה markdown formatting
    raw = re.sub(r'```json\n?', '', raw)
    raw = re.sub(r'```\n?', '', raw)
    raw = raw.strip()
    
    # הסר כל טקסט שלפני או אחרי ה-JSON
    match = re.search(r'\[\s*\{.*\}\s*\]', raw, re.DOTALL)
    if match:
        raw = match.group(0)
    
    print(f"DEBUG - Cleaned response:\n{raw}\n")
    
    data = json.loads(raw)
    return [Requirement(**r) for r in data]
"""Requirements extractor module."""
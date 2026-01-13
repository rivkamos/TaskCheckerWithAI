# analysis/requirement_checker.py
from models.result import RequirementResult
from llm.base import LLMClient

def check_requirement(req, code_snapshot: str, llm: LLMClient) -> RequirementResult:
    prompt = f"""
    דרישה:
    {req.description}

    קוד הפרויקט:
    {code_snapshot}

    ענה:
    - האם הדרישה ממומשת (כן/לא)
    - הסבר קצר
    """

    answer = llm.complete(prompt)

    fulfilled = "כן" in answer.splitlines()[0]

    return RequirementResult(
        requirement_id=req.id,
        fulfilled=fulfilled,
        explanation=answer
    )
"""Requirement checker module."""
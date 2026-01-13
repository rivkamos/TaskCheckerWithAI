# models/result.py
from dataclasses import dataclass

@dataclass
class RequirementResult:
    requirement_id: str
    fulfilled: bool
    explanation: str
"""Requirement result data model module."""
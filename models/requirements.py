# models/requirements.py
from dataclasses import dataclass

@dataclass
class Requirement:
    id: str
    description: str
    category: str
"""Requirement data model module."""
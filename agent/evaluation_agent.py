# agent/evaluation_agent.py
from analysis.snapshot_builder import build_code_snapshot
from analysis.project_validator import validate_project
from analysis.requirements_extractor import extract_requirements
from analysis.requirement_checker import check_requirement

class EvaluationAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, task_text, project_path):
        requirements = extract_requirements(task_text, self.llm)
        technical_issues = validate_project(project_path)
        snapshot = build_code_snapshot(project_path)

        results = [
            check_requirement(req, snapshot, self.llm)
            for req in requirements
        ]

        return technical_issues, results
"""Evaluation agent module."""
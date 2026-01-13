# cli.py
import argparse
import os
from dotenv import load_dotenv
from pathlib import Path

# from llm.openai_client import OpenAIClient

from llm.gemini_client import GeminiClient
from ingestion.task_file_loader import load_task_file
from ingestion.git_repo_loader import clone_repo
from agent.evaluation_agent import EvaluationAgent

load_dotenv()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--workdir", default="workspace")

    args = parser.parse_args()

    workdir = Path(args.workdir)
    repo_dir = workdir / "repo"

    task_text = load_task_file(args.task)
    clone_repo(args.repo, repo_dir)

    # llm = OpenAIClient(api_key=os.environ["OPENAI_API_KEY"])
    llm = GeminiClient(api_key=os.environ["GOOGLE_API_KEY"])
    agent = EvaluationAgent(llm)

    tech_issues, results = agent.run(task_text, repo_dir)

    print("\n=== בעיות טכניות ===")
    for i in tech_issues:
        print("-", i)

    print("\n=== בדיקת דרישות ===")
    for r in results:
        status = "✔" if r.fulfilled else "✖"
        print(f"{status} {r.requirement_id}: {r.explanation}")

if __name__ == "__main__":
    main()
"""Command-line interface for the requirement evaluation agent."""
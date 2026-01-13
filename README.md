# ReqAgent - Requirement Evaluation Agent

An automated system for analyzing and evaluating software project requirements against actual code implementation.

## 📋 Description

ReqAgent is a tool that uses artificial intelligence (Gemini/OpenAI) to:
- Extract requirements from task documents
- Verify requirement implementation in code
- Generate comprehensive reports on requirement fulfillment

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd ReqAgent

### Prerequisites
2. Create a virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or: source venv/bin/activate  # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file:

OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_key_here

💻 Usage

Command Line
python cli.py --task task.txt --repo https://github.com/your-repo.git --workdir workspace

Parameters
--task (required): Path to the task file
--repo (required): URL of the repository to clone
--workdir (optional): Working directory (default: workspace)
Run with Debugger
Press F5 in VS Code or select "Python Debugger: Current File with Arguments"

📁 Project Structure
ReqAgent/
├── cli.py                          # Command-line interface
├── requirements.txt                # Project dependencies
├── agent/
│   └── evaluation_agent.py         # Main evaluation agent
├── analysis/
│   ├── requirements_extractor.py   # Extract requirements
│   ├── requirement_checker.py      # Check requirements
│   ├── project_validator.py        # Validate project
│   └── snapshot_builder.py         # Build code snapshot
├── ingestion/
│   ├── git_repo_loader.py          # Load repository from Git
│   └── task_file_loader.py         # Load task file
├── llm/
│   ├── base.py                     # Base LLM interface
│   ├── openai_client.py            # OpenAI client
│   └── gemini_client.py            # Google Gemini client
├── models/
│   ├── requirements.py             # Requirement model
│   └── result.py                   # RequirementResult model
└── output/
    └── report_generator.py         # Report generation


🔧 Configuration
Choosing LLM Provider
Update cli.py to choose between Gemini or OpenAI:

For Gemini (default):
llm = GeminiClient(api_key=os.environ["GOOGLE_API_KEY"])

For OpenAI:
from llm.openai_client import OpenAIClient
llm = OpenAIClient(api_key=os.environ["OPENAI_API_KEY"])


📊 Output
Results are printed to the terminal:
=== Technical Issues ===
- [Issue 1]
- [Issue 2]

=== Requirements Check ===
✔ REQ-1: [Explanation]
✖ REQ-2: [Explanation]

🐛 Debugging
Open launch.json
Update the values:
--task: Your task file name
--repo: Your repository URL
Press F5 to run with debugger
📦 Dependencies
openai - OpenAI API
python-dotenv - Environment variable management
google-generativeai - Google Gemini API
🔒 Security
Never share the .env file: It contains secret API keys
The .env file is hidden from Git (see .gitignore)
Use secure secrets management in production
🤝 Contributing
Suggestions welcome! Submit pull requests with improvements.

📝 License
[Add your license here]

📧 Contact
Questions? Open an issue in the repository!

Note: This is a development tool. Results may require manual review.
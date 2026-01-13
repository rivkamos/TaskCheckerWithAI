# output/report_generator.py
def generate_report(results: dict) -> str:
    report = []
    report.append("דו״ח בדיקת פרויקט\n")

    for r in results["requirements"]:
        report.append(str(r))

    if results["technical_issues"]:
        report.append("\nבעיות טכניות:")
        report.extend(results["technical_issues"])

    return "\n".join(report)
"""Report generator module."""

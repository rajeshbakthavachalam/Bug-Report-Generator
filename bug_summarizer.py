import subprocess

def generate_bug_report(description: str, severity: str, model: str) -> str:
    prompt = f"""
You are a QA assistant. Convert the following bug description into a clear, structured JIRA-style bug report.

---

Bug Description:
"{description}"

Severity: {severity}

---

Format:

**Summary:**
<one-line summary>

**Steps to Reproduce:**
1. Step 1
2. Step 2
...

**Expected Result:**
<expected>

**Actual Result:**
<actual>

**Severity:**
{severity}

**Environment:**
- Browser:
- OS:
- App Version:

**Attachments:**
N/A
"""
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

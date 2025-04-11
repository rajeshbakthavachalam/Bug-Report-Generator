"# Bug-Report-Generator" 
# 🪲 AI-Powered Bug Report Generator (PoC)

Transform raw bug descriptions into clean, structured, Jira-ready reports using local LLMs like **LLaMA 3.2** and **DeepSeek**, running via **Ollama**.

---

## 🔍 Overview

This is a **Proof of Concept (PoC)** designed to simplify one of the most time-consuming tasks in software testing: writing detailed bug reports.

Instead of manually formatting summaries, reproduction steps, and environment info, just drop in a raw bug description like:

> "The login button doesn’t respond on Chrome browser"

…and instantly generate a polished bug report that includes:

- ✅ Summary  
- 🔁 Steps to Reproduce  
- 🎯 Expected vs Actual Results  
- 🚦 Severity  
- 🌐 Environment Info

Just copy → paste into Jira, Azure DevOps, or any tracker.

---

## 🧠 Powered By

- 🔥 [LLaMA 3.2](https://ollama.com/library/llama3) & [DeepSeek](https://ollama.com/library/deepseek-r1) via [Ollama](https://ollama.com/)
- 🖥️ [Streamlit](https://streamlit.io/) for a clean, interactive UI
- 🐍 Python + `subprocess` for local model integration

---

## 📸 Demo

🎥 **Video demo coming soon!**  
A walkthrough showcasing how this tool works in real-time.

---

## 🚀 Features

- Paste any raw bug description and generate a structured report
- Choose between `llama3.2` and `deepseek-r1`
- Download or copy the generated bug report
- Ideal for browser bugs, mobile apps, network testing, and more
- Fully local — no internet/API key required if using Ollama

---

## 🧱 Project Structure

![alt text](image.png)


---

## 📦 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/rajeshbakthavachalam/Bug-Report-Generator.git
cd Bug-Report-Generator

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux

3.Install Python dependencies
pip install -r requirements.txt

4.Install & run the model(s) via Ollama

ollama pull llama3.2
# or
ollama pull deepseek-r1

5.Start the Streamlit app

streamlit run app.py

 Roadmap / Coming Soon
🧠 Fine-tuned models using real-world Jira bug data

🔍 Retrieval-Augmented Generation (RAG) using internal documentation

📊 CI/CD integration to auto-summarize failed test logs

🧪 Suggested test cases per bug

🔁 Duplicate bug detection & triage recommendations

🤝 Contributions
Contributions are welcome!
Feel free to fork this project, suggest new features, or raise issues to improve functionality.


🙌 Acknowledgements
Meta AI – LLaMA
DeepSeek
Streamlit
Ollama



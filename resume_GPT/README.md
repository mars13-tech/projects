# 📄 ResumeGPT – Instantly Improve Your Resume Using GPT-3.5

**ResumeGPT** is a Python tool and web app that enhances your resume using OpenAI's GPT-3.5. It rewrites your resume to be more professional, polished, and ATS-friendly — instantly.

---

## 🔧 Features

- ✅ Paste your raw resume text
- ✅ GPT-3.5 transforms it for job-readiness
- ✅ Streamlit web UI included
- ✅ Beginner-friendly and easy to run
- ✅ Modular code structure (CLI or Web)

---

## 📦 What You Get

- `resume_gpt.py` – GPT-based resume improver logic
- `resume_web.py` – Streamlit-powered web interface
- `README.md` – Setup & usage instructions

---

## 💡 Requirements

- Python 3.7 or higher
- OpenAI API key  
  👉 [Get one here](https://platform.openai.com/account/api-keys)
- Python packages:
  ```bash
  pip install openai streamlit os
```

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Download or Clone the Project

```bash
cd path/to/your/projects/folder
```

### 🔹 Step 2: Install Dependencies

```bash
pip install openai streamlit os
```

### 🔹 Step 3: Set Your API Key

**Windows:**

```bash
set OPENAI_API_KEY=your-api-key-here
```

**macOS/Linux:**

```bash
export OPENAI_API_KEY=your-api-key-here
```

---

## 🚀 Option A: Run the Streamlit Web App

```bash
cd resume_GPT
streamlit run resume_web.py
```

---

## 🧪 Option B: Use as a Command-Line Tool (CLI)

Create a file named `test_cli.py`:

```python
from resume_gpt import improve_resume

with open("raw_resume.txt", "r") as f:
    resume = f.read()

improved = improve_resume(resume)

with open("improved_resume.txt", "w") as f:
    f.write(improved)

print("✅ Improved resume saved as improved_resume.txt")
```

Then run:

```bash
python test_cli.py
```

---

## 🔒 Disclaimer

* 🔑 You must use your own **OpenAI API key** (not included)
* 🤖 Powered by GPT-3.5 via OpenAI API
* 📝 Resume quality depends on the quality of your input

---

## 🧠 Ideal For

* Job seekers 🧑‍💻
* Freelancers ✍️
* Students & freshers 👨‍🎓
* Developers building personal projects
* Anyone wanting to optimize their resume with AI

---

## 🙌 Contribute

Feel free to fork, customize, or extend ResumeGPT for your own use.
PRs and feedback welcome!

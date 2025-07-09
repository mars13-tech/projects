ResumeGPT — Instantly Improve Your Resume Using GPT

This tool helps you instantly upgrade your resume using GPT-3.5.

---

🛠 What It Does

- Reads your resume from `raw_resume.txt`
- Sends it to GPT-3.5 with a prompt
- Saves the improved resume in `improved_resume.txt`

---

📦 What's Included

- `main.py` — the core script  
- `README.md` — setup instructions  
You will create `raw_resume.txt` and `improved_resume.txt` as part of setup.

---

💡 Requirements

- Python 3.7+
- OpenAI account and API key

---

🔧 How to Use

1. Create files:
raw_resume.txt inside the file enter your resume details
improved_resume.txt In a same main.py folder

1. Install OpenAI library:
```bash
pip install openai
pip install os

2. Get your API key from:
https://platform.openai.com/account/api-keys

3. Set your API key in terminal:

Windows:
set OPENAI_API_KEY=your-key-here

macOS/Linux:
export OPENAI_API_KEY=your-key-here

4. Run the tool:
python main.py

GPT Assistant v0.2 🤖

GPT Assistant v0.2 is a Python-based AI assistant that can hold a **conversation with memory** using OpenAI's GPT-3.5 model. It remembers your previous questions and answers, making interactions more natural — just like talking to a real assistant.


🚀 Features

- Interactive chat loop (type and get responses instantly)
- Assistant remembers full conversation history
- Powered by OpenAI GPT-3.5 (`gpt-3.5-turbo`)
- Exits when you type `exit` or `quit`


🧠 How It Works

The assistant uses a list called `conversation` to store the full chat history:

```python
conversation = [
    {"role": "system", "content": "You are a helpful AGI assistant."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I help you?"},
    ...
]
Each message is sent to OpenAI API so the assistant replies with full context.

🛠️ Setup Instructions

1. Install OpenAI SDK
pip install openai

2. Set Your OpenAI API Key
Replace "your-api-key-here" with your actual API key:
openai.api_key = "sk-..."  # from https://platform.openai.com/account/api-keys

3. Run the Assistant
python gpt_assistant_v0_2.py

📄 Example

You: Hi
AGI Assistant: Hello! How can I assist you today?

You: What is Python?
AGI Assistant: Python is a high-level programming language...

💡 Learning Purpose
This version is a stepping stone to building full AGI systems. It teaches:

   1.API usage

   2.Chat history management

   3.Role-based message formatting

   4.Input/output handling in Python

📜 License
MIT License — use it, improve it, share it!

🙏 Credits
Built by Karthi Keyan as part of a personal AGI learning journey.
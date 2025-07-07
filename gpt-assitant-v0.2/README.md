```markdown
# GPT Assistant v0.2 🤖

GPT Assistant v0.2 is a Python-based AI assistant that can hold a conversation with memory using OpenAI's GPT-3.5 model.

## 🚀 Features

- Multi-turn chat with memory
- Real-time user input and assistant response
- Uses OpenAI's gpt-3.5-turbo model
- Clean exit with "exit" or "quit"

## 🛠️ Setup

1. Install OpenAI Python SDK:
```

pip install openai

````

2. Replace your API key in the script:
```python
openai.api_key = "your-api-key-here"
````

3. Run the script:

   ```
   python gpt_assistant_v0_2.py
   ```

## 📄 Example

```
You: Hello
AGI Assistant: Hello! How can I assist you today?

You: Tell me a joke
AGI Assistant: Why don't scientists trust atoms? Because they make up everything!
```

## 📚 How It Works

All messages are stored in a `conversation` list with roles: `system`, `user`, and `assistant`. This history is sent to GPT on each request for context-aware replies.

## 🧱 Roadmap

* v0.1: Single-turn assistant
* ✅ v0.2: Multi-turn memory

## 🧠 Author

Built by Karthi Keyan as part of an AGI learning journey.

```
```

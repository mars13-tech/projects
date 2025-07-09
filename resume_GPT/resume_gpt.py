import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def improve_resume(resume_text):
    prompt = f"""You are a resume expert. Improve this resume text:
---
{resume_text}
---
Make it more ATS-optimized and professional."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

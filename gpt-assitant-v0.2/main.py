import openai
openai.api_key = "your-api-key-here"

# Start the conversation history
conversation = [
    {"role": "system", "content": "You are a helpful AGI assistant."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user's message to conversation
    conversation.append({"role": "user", "content": user_input})

    # Get GPT response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract reply text
    reply = response["choices"][0]["message"]["content"]
    print("AGI Assistant:", reply)

    # Add assistant reply to conversation
    conversation.append({"role": "assistant", "content": reply})

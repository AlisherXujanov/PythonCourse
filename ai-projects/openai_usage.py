# pipenv install openai


from openai import OpenAI
import os

# Set your API key here
API_KEY = ''

# Initialize the OpenAI API client

client = OpenAI(
    # This is the default and can be omitted
    api_key=API_KEY,
)

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input("Enter your question here ...:  "),
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion)
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(e)
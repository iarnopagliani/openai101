import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

question = input ("Ask me something: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": f"{ question }"},
    ]
)
answer = ''
for choice in response.choices:
    answer += choice.message.content
print(f"We asked chatGPT { question } - here is their response: ")
print(answer)

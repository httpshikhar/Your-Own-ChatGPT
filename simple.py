import os
import openai
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

message = []
client = OpenAI()
openai.api_key = os.getenv("OPEN_API_KEY")

response1 = input("Enter the type of gpt you want : ")
message.append({"role": "system", "content": response1})

print("Your new assistant at your service")

while input != "quit()":
    reponse2 = input()
    message.append({"role": "user", "content": reponse2})
    reply = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )
    reponse = reply["choices"][0]["message"]["content"]
    message.append({"role": "assistant", "content": reply})
    print("\n" + reponse + "\n")


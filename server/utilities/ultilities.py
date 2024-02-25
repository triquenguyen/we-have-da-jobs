from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def getKeyWords(description):
    system = open('server/system_query.txt')
    user = open('server/user_query.txt')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system.read() + description},
            {"role": "user", "content": user.read()}
        ])
    return (response.choices[0].message.content).split(', ')
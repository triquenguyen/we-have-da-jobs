from openai import OpenAI
import os


client = OpenAI(api_key="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")

def getKeyWords(description):
    # system = open('server/utilities/system_query.txt')
    # user = open('server/utilities/user_query.txt')
    system = "You are a recruiter who writes this job description for the designer role."
    user = "From the job post, extract all of the keywords that are important for the candidate to have into 1 string. Each keyword is separated by comma."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system + description},
            {"role": "user", "content": user}
        ])
    return (response.choices[0].message.content).split(', ')
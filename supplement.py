import requests
import json
import openai

#def api(prompt):
def get_remedies(user_input):
    prompts = []
    response = []
    prompt = "Remedies, natural healthy food, yoga exercise for " + user_input +  ". Give the output in 3 separate blocks of paragraph with points in each paragraph."
    # prompt1 = 'Best 5 useful Natural foods for ' + user_input
    # prompt2 = 'Best 5 useful Yoga excersizes for ' + user_input
    # prompt3 = 'Best 5 useful Ayurvedic natural supplements for ' + user_input
    # prompts.append(prompt1)
    # prompts.append(prompt2)
    # prompts.append(prompt3)

    openai.api_key = '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'
    messages = [{"role": "system", "content": "You are an intelligent assistant."}]

    # for i in range(len(prompts)):
    #     message = prompts[i]
    message = prompt


    # message = f'Please write a remedy for {}'
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    response = chat.choices[0].message.content
    # reply = list(map(str, reply.split('')))
    # reply = reply.split("Paragraph 1")
    # reply = [p.strip() for p in reply if p.strip()]

    # for i, j in enumerate(reply, start=1):
    #     response.append(f"Para
    # graph {i}: {reply}")
    # response.append(reply)

    response = str(response)
    response = response.split("\n")
    # for i in response:
    #     i = i.split("\n")
    # prompt = str(prompt)
    
    return response

'''


'''

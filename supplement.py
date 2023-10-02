import requests
import openai
import os

#def api(prompt):
def get_remedies(user_input):
    prompts = []
    response = []
    prompt = "Remedies, natural healthy food, yoga exercise for " + user_input +  ". Give the output in 3 separate blocks of paragraph with points in each paragraph."
    
    key = os.getenv(API_key, default = None)
    openai.api_key = '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'
    messages = [{"role": "system", "content": "You are an intelligent assistant."}]

    # for i in range(len(prompts)):
    #     message = prompts[i]
    message = prompt



    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    response = chat.choices[0].message.content


    response = str(response)
    response = response.split("\n")
    # for i in response:
    #     i = i.split("\n")
    # prompt = str(prompt)
    
    return response

'''


'''

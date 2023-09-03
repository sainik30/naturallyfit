import requests
import json
import openai

#def api(prompt):
def get_remedies(user_input):
    prompts = []
    response = []
    prompt1 = 'Best 5 useful Natural foods for ' + user_input
    prompt2 = 'Best 5 useful Yoga excersizes for ' + user_input
    prompt3 = 'Best 5 useful Ayurvedic natural supplements for ' + user_input
    prompts.append(prompt1)
    prompts.append(prompt2)
    prompts.append(prompt3)

    openai.api_key = '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'
    messages = [{"role": "system", "content": "You are an intelligent assistant."}]

    for i in range(len(prompts)):
        message = prompts[i]

    # message = f'Please write a remedy for {}'
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        # reply = list(map(str, reply.split('')))
        response.append(reply)

   
    return response


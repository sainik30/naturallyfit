import requests
import openai

#def api(prompt):
def get_remedies(user_input):
    prompts = []
    response = []
    prompt = "Remedies, natural healthy food, yoga exercise for " + user_input +  ". Give the output in 3 separate blocks of paragraph with points in each paragraph."

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

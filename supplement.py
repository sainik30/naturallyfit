import requests
import json
import openai

#def api(prompt):
def get_remedies(user_input):
    response = []
    response1 = 'Best 5 useful Natural food items for ' + user_input
    response2 = 'Best 5 useful Yoga for ' + user_input
    response3 = 'Best 5 useful Ayurvedic remedies for ' + user_input
    response.append(response1)
    response.append(response2)
    response.append(response3)

    return response

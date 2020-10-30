import requests

def generate_new_token():
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://interview.agileengine.com/auth', json={"apiKey": "23567b218376f79d9415"}, headers=headers)
    return response.json()['token']

current_token = generate_new_token()

def update_current_token():
    current_token = generate_new_token()

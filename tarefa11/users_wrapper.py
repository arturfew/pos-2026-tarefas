import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def list():
    resposta = requests.get(API_URL)
    if resposta.status_code == 200:
        return resposta.json()
    return []

def read(user_id):
    resposta = requests.get(f"{API_URL}/{user_id}")
    if resposta.status_code == 200:
        return resposta.json()
    return None

def create(user_data):
    resposta = requests.post(API_URL, json=user_data)
    if resposta.status_code == 201:
        return resposta.json()
    return None

def update(user_id, user_data):
    resposta = requests.put(f"{API_URL}/{user_id}", json=user_data)
    if resposta.status_code == 200:
        return resposta.json()
    return None

def delete(user_id):
    resposta = requests.delete(f"{API_URL}/{user_id}")
    return resposta.status_code in (200, 204)
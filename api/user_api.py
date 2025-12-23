import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    return requests.get(url).json()

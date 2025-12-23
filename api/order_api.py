import requests

def get_orders():
    url = "https://fakestoreapi.com/carts"
    return requests.get(url).json()

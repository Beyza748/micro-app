import requests

def get_products():
    url = "https://fakestoreapi.com/products"
    return requests.get(url).json()

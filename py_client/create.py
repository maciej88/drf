import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.post(endpoint, json=data)

data = {
    "title": "done!",
    "price": 32.99
}
print(get_response.text)
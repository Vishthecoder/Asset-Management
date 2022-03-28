import requests

api_url = "http://127.0.0.1:8000/api/44442222/"
response = requests.get(api_url)
print(response.json())

todo = {"location": 3}
response = requests.patch(api_url, json=todo)
print(response.json())
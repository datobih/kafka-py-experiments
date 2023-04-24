import requests


response=requests.post('http://127.0.0.1:8000/microservice-one/',json='Hey bitch')
print(response)
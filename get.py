# - **********************************************************
# - Author: Suchin T
# - Date: 2024-09-26 (YYYY-MM-DD)
# - Version: 0.1
# - Function: CMD Application to communicate request 
#   method GET with Server 
# - **********************************************************

import requests

Version = "0.1"

url_local = 'http://127.0.0.1:8000/api/get'

response = requests.get(url_local)

print(f"** CMD Application : GET Request ver ... {Version}")
print(f"** Connect to server path : {url_local}")
print("** ------------------------------------------------------")
print(f'response.content = {response.content}')
print(f'response.status_code = {response.status_code}')
print(f'response.text = {response.text}')
print(f'type(response.json()) = {type(response.json())}')
print(f'response.json() = {response.json()}')
print(f'type(response.headers) = {type(response.headers)}')
print(f"response.headers['Content-type'] = {response.headers['Content-type']}")
print(f'response.headers = {response.headers}')
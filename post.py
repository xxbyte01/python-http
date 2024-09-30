# - **********************************************************
# - Author: Suchin T
# - Date: 2024-09-26 (YYYY-MM-DD)
# - Version: 0.1
# - Function: CMD Application to communicate request 
#   method POST with Server 
# - **********************************************************

import requests

Version = "0.1"

url_local = 'http://127.0.0.1:8000/api/post'

data_send = {"name":"Sukiyaki", "age": 46, "wise":True}
resp = requests.post(url_local,json=data_send)

print(f"** CMD Application : POST Request ver ... {Version}")
print(f"** Connect to server path : {url_local}")
print("** ------------------------------------------------------")
print(f'resp.status_code = {resp.status_code}')
print(f'resp.text = {resp.text}')
import json
import requests

base_url = "http://127.0.0.1:8000/api/updateItem/4/"

id = 4

data = {
        "design_path":"xxx"
}


reply = requests.post(base_url , data=data)

print(reply.json)
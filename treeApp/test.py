import datetime
import requests

base_url = "http://127.0.0.1:8000/orders/"
d = datetime.date(1997, 10, 19)
data = """{
        "user_id": 1,
        "client_id": 1,
        "recived_date": "2022-05-28",
        "delivery_date": "2022-09-28",
        "design_types": "A",
        "design_path": "ddddddd",
        "design_category": [
            "x"
        ],
        "printing_type": [
            "x"
        ],
        "size_width": 56.0,
        "size_high": 645.0,
        "materials": "dsaaa",
        "color": "asddddd",
        "thickness": 12.2,
        "Post_print_services": [
            "x"
        ],
        "state": "D",
        "notes": "asd"

    }"""

# print(d)
headers = {'Accept': '*/*; indent=4', 'Content-Type': 'application/json',
           'Authorization': 'Token 497d1a25281fa5809049fdb30939658bbe9b78a7'}



post = requests.post(base_url , data=data , headers=headers).json()
print(post)

# get = requests.get(base_url)
# print(get.json())

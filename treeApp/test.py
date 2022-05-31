import datetime
import requests

base_url = "http://127.0.0.1:8000/orders/"
d = datetime.date(1997, 10, 19)
data = {
        "recived_date": d,
        "delivery_date": d,
        "design_types": "A",
        "design_path": "dsf",
        "design_category": ["x"],
        "printing_type": ["x"],
        "size_width": 56.0,
        "size_high": 645.0,
        "materials": "645",
        "color": "gdf",
        "thickness": 12.2,
        "Post_print_services": ["x"],
        "state": "D",
        "notes": "asd",
        "user_id": 2,
        "client_id": 1
    }

headers = {'Accept': '*/*; indent=4', 'Content-Type': 'application/json',
           'Authorization': 'Token 2a78f3a94598e77134f4bd9e5abe219859646fe0'}



post = requests.post(base_url , data=data , headers=headers).json()
print(post)

# get = requests.get(base_url)
# print(get.json())

import datetime
import requests

base_url = "http://127.0.0.1:8000/orders/"
d = datetime.date(1997, 10, 19)
data =     {
        "recived_date": d,
        "delivery_date": d,
        "design_types": "A",
        "design_path": "dsf",
        "design_category": [
            "x"
        ],
        "printing_type": [
            "x"
        ],
        "size_width": 125.0,
        "size_high": 125.0,
        "materials": "sdf",
        "color": "dsf",
        "thickness": 12.0,
        "Post_print_services": [
            "x"
        ],
        "state": "D",
        "notes": "asd",
        "user_id": "saied",
        "client_id": "zabbix"
    }

r = requests.post(base_url , data)
print(r)
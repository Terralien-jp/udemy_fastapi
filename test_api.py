import requests
import json

def main():
    url = 'http://127.0.0.1:8000/item/'
    body = {
        "name": "Yakiimo",
        "description": "焼いた芋",
        "price": 590,
        "tax": 1.1
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())

if __name__ == "__main__":
    main()
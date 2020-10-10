import requests
import base64
import json
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('API_KEY') \
    or os.environ.get("AWS_S3_ACCESS_KEY_ID")

api_base_url = "https://gw.hackathon.vtb.ru/vtb/hackathon"

def car_recognize_method(image):    
    url = f"{api_base_url}/car-recognize"
    image = base64.b64encode(image).decode()
    headers = {"accept": "application/json", "content-type": "application/json", "x-ibm-client-id": key}
    data = {"content": image}
    r = requests.post(url, data = json.dumps(data), headers = headers)

    if r.status_code == 200:
        return json.loads(r.text)
    return r.text

def get_marketplace_data():
    url = f"{api_base_url}/marketplace"
    headers = {"accept": "application/json", "content-type": "application/json", "x-ibm-client-id": key}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    return r.text

def car_loan_method(data):
    url = f"{api_base_url}/carloan"
    headers = {"accept": "application/json", "content-type": "application/json", "x-ibm-client-id": key}
    data = data
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    return r.text

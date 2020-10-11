import requests
import base64
import json
from dotenv import load_dotenv
import os
from .utils import *

load_dotenv()

key = os.getenv("API_KEY") \
      or os.environ.get("AWS_S3_ACCESS_KEY_ID")

# Api request constants
api_base_url = "https://gw.hackathon.vtb.ru/vtb/hackathon"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-ibm-client-id": key
}


def car_recognize_method(image):
    url = f"{api_base_url}/car-recognize"
    data = {"content": image}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        cars = json.loads(r.text).get("probabilities")
        cars = list(cars.items())
        cars.sort(key=lambda i: i[1], reverse=True)
        return cars[0]
    return r.text


# def get_marketplace_data():
#     url = f"{api_base_url}/marketplace"
#     r = requests.get(url, headers=headers)
#
#     if r.status_code == 200:
#         return json.loads(r.text)
#     return r.text

def request_vtb_api(data, method):
    url = f"{api_base_url}/{method}"
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    return r.text


def calculate(data):
    url = f"{api_base_url}/calculate"
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)
    return r.text


def car_loan_method(data):
    url = f"{api_base_url}/carloan"
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if r.status_code == 200:
        return json.loads(r.text)

    return r.text


def payments_graph_method(data):
    url = f"{api_base_url}/payments-graph"
    r = requests.post(url, data = json.dumps(data), headers = headers)

    if r.status_code == 200:
        data = json.loads(r.text)

        payments = data.get('payments')
        data['payments'] = trimPaymentsGraph(payments)

        return data
    
    return r.text



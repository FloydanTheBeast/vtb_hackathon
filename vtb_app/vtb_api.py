import requests
import base64
import json

key = "430664873e716b7b8243ea2f2c464f6f"
url = "https://gw.hackathon.vtb.ru/vtb/hackathon/car-recognize"


def car_recognize_method(image):
    image = base64.b64encode(image).decode()
    headers = {"accept": "application/json", "content-type": "application/json", "x-ibm-client-id": key}
    data = {"content": image}
    r = requests.post(url, data = json.dumps(data), headers = headers)

    if r.status_code == 200:
        cars = json.loads(r.text).get("probabilities")
        cars = list(cars.items())
        cars.sort(key = lambda i: i[1], reverse = True)
        return cars[0]
    else:
        return r.text

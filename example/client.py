import requests
import json
import base64
from io import BytesIO
from PIL import Image

url = "http://127.0.0.1:8000/generation"

with open("./input.jpeg", "rb") as image_file:
    image_data = image_file.read()
input_image_str = base64.b64encode(image_data).decode('utf-8')

data = {
    "request_id": 1234,
    "text": "a muscle man",
    "input_image_base64": input_image_str,
    "random_seed": 5678
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Generated ID:", result["request_id"])
    output_image_str = result["output_image_base64"]
    pic = Image.open(BytesIO(base64.b64decode(output_image_str)))
    pic.save("response.jpeg")
else:
    print("Failed to process the request. Status code:", response.status_code)

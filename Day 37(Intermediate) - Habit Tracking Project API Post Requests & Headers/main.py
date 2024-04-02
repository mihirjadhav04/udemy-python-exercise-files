import requests
from datetime import datetime

USERNAME = "mihirjadhv04"
TOKEN = "jafdslkhfaioehoinfkl"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response)

PIXEL_POINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

today = datetime(year=2021, month=11, day=13)
date = today.strftime("%Y%m%d")
# print(today.strftime("%Y%m%d"))
pixel_params = {
    "quantity": "2",
}


# response = requests.post(url=PIXEL_POINT, json=pixel_params, headers=headers)

# response = requests.put(url=f"{PIXEL_POINT}/{date}", json=pixel_params, headers=headers)
# print(response.text)


delete_pixel_endpoint = f"{PIXEL_POINT}/{date}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

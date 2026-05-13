import requests
import datetime as dt
USERNAME = "x"
TOKEN = "x"
GRAPH_ID = "graph01"
pixela_endpoint = "https://pixe.la/v1/users"

today = dt.date.today().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN" : TOKEN,
}

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph01",
    "name": "Learning Graph",
    "unit": "hours",
    "type": "float",
    "color": "ichou"
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date" : today,
    "quantity" : "6"
}

#response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(response.text)

pixel_update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.put(url=pixel_update_endpoint, json=pixel_config, headers=headers)
print(response.text)

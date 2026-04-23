import requests
from datetime import datetime

pixela_URL = "https://pixe.la/v1/users"
token = "sdf09fsd7sdf90sf80as"
user = "mir6"
api_key = ""
grap_id = "graph01"

params = {
    "token":token,
    "username":user,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    
}

# res = requests.post(url=pixela_URL, json=params)
# print(res.text)
graph_url = f"{pixela_URL}/{user}/graphs/"

graph_conf = {
    "id":"graph01",
    "name":"cycling",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
header = {
    "X-USER-TOKEN":token,
}

# res = requests.post(url=graph_url, json=graph_conf, headers=header)
# print(res.text)

pixel_endpoint = f"{pixela_URL}/{user}/graphs/{grap_id}"
today = datetime.now()

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"12.10",
}
res = requests.post(url= pixel_endpoint, json= pixel_data, headers=header)
print(res.text)
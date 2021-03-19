import requests
import config
from datetime import datetime

USER_ENDPOINT = "https://pixe.la/v1/users"
# USER_PARAMETERS = {
#     "token": config.pixela_token,
#     "username": config.pixela_ursername,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# Creating a user
# create_user = requests.post(url=USER_ENDPOINT, json=USER_PARAMETERS)
# create_user.raise_for_status()
# print(create_user.text)


GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{config.pixela_ursername}/graphs"
headers = {
     "X-USER-TOKEN": config.pixela_token
}
# GRAPH_PARAMETERS = {
#     "id": "graph1",
#     "name": "practices",
#     "unit": "days",
#     "type": "int",
#     "color": "ajisai"
# }
# Creating a new graph
# create_graph = requests.post(url=GRAPH_ENDPOINT, headers=headers, json=GRAPH_PARAMETERS)
# create_graph.raise_for_status()
# print(create_graph.text)

# Get the graph
"Visit the url: https://pixe.la/v1/users/ecanro/graphs/graph1.html"

#Add a pixel
GRAPH_ID = "graph1"
GRAPH_ENDPOINT_PIXEL = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
today = datetime(year=2021, month=3, day=6)
PIXEL_PARAMETERS = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

# add_pixel = requests.post(url=GRAPH_ENDPOINT_PIXEL, headers=headers, json=PIXEL_PARAMETERS)
# print(add_pixel.text)

# Update Pixel
PIXEL_DATA = today.strftime("%Y%m%d")
UPDATE_PARAMETERS = {
    "quantity": "2"
}
update_pixel = requests.put(url=f"{GRAPH_ENDPOINT_PIXEL}/{PIXEL_DATA}", headers=headers, json=UPDATE_PARAMETERS)
print(update_pixel)

# Delete pixel or graph
requests.delete(url=f"{GRAPH_ENDPOINT_PIXEL}/{PIXEL_DATA}", headers=headers)
requests.delete(url=f"{GRAPH_ENDPOINT_PIXEL}", headers=headers)

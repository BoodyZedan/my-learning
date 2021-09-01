import requests
from datetime import datetime

username = "boodyzedan"
token = "fkyljgklfajlkjgjfklidajkl"

pixela_endpoint = "https://pixe.la/v1/users"

user_prams = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_prams)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "abdallah5",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": token
}

today = datetime.now().strftime("%Y%m%d")

# response = requests.post(url=pixela_endpoint, json=user_prams)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/abdallah5"

pixel_data = {
    "date": today,
    "quantity": input("How meany Kms did you cycle today?:")
}

pixel_headers = {
    "X-USER-TOKEN": token
}


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=pixel_headers)
print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{username}/graphs/abdallah5/{today}"

pixel_put_data = {
    "quantity": "0.0"
}

pixel_put_headers = {
    "X-USER-TOKEN": token
}


# response = requests.put(url=pixel_put_endpoint, json=pixel_put_data, headers=pixel_put_headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/abdallah5/20210831"

pixel_delete_data = {
    "quantity": "0.0"
}

pixel_delete_headers = {
    "X-USER-TOKEN": token
}


# response = requests.delete(url=pixel_delete_endpoint, json=pixel_delete_data, headers=pixel_delete_headers)
# print(response.text)

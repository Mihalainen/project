import requests

import config
import data


def post_new_user(body):
    return requests.post(config.URL + config.CREATE_USER,
                         json=body,
                         headers=data.header)


def get_new_token():
    user_response = post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

def new_kit_body():
    change_kit_body = data.kit_body.copy()
    change_kit_body["name"] = "AAAA"
    return change_kit_body

def new_header():
    new_header=data.header.copy()
    new_header["Authorization"] = get_new_token()
    return new_header

def create_new_kit(get_new_token):
    headers = data.header.copy()
    headers["Authorization"] = "Bearer " + get_new_token()
    body = new_kit_body()
    return requests.post(config.URL+config.CREATE_KITS, json=body, headers=headers)
response = create_new_kit(get_new_token).json()["name"]

def test1():
    assert response == new_kit_body()["name"]



import requests
from jsonschema import validate


# GET
def get_users(api_url, headers, page="2"):
    response = requests.get(api_url + f"/api/users/{page}", headers=headers)
    return response

def get_user_by_id(api_url, headers, name, job, user_id="2"):
    response = requests.get(api_url + f"/api/users/{user_id}", headers=headers)
    body = response.json()
    print(body)
    assert body["data"]["first_name"] == name
    assert body["data"]["last_name"] == job
    return body

def get_non_existent_users(api_url, headers, user_id="23"):
    response = requests.get(api_url + f"/api/users/{user_id}", headers=headers)
    return response


def get_unknown_methode(api_url, headers, user_id="23"):
    response = requests.get(api_url + f"/api/unknown/{user_id}", headers=headers)
    return response


def get_incomplete_url(api_url, headers):
    response = requests.get(api_url + "api", headers=headers)
    return response


# POST
def post_users_should_be_create(api_url, headers, name=str, job=str):
    response = requests.post(api_url + "/api/users", headers=headers, data={"name": name, "job": job})
    body = response.json()
    assert body["name"] == name
    assert body["job"] == job
    return response, body


def post_verify_users_creation_fails(api_url):
    response = requests.post(api_url + "/api/users")
    return response


def post_create_users_data_empty(api_url, headers):
    response = requests.post(api_url + "/api/users", headers=headers, data={})
    body = response.json()
    assert 'name' not in body
    assert 'job' not in body
    return response


# PUT
def put_update_users(api_url, headers, name, job, user_id="2"):
    response = requests.put(api_url + f"/api/users/{user_id}", headers=headers, data={"name": name, "job": job})
    body = response.json()
    assert body["name"] == name
    assert body["job"] == job
    return response, body


# PATCH
def patch_update_user_name(api_url, headers, name, user_id="2"):
    response = requests.patch(api_url + f"/api/users/{user_id}", headers=headers, data={"name": name})
    body = response.json()
    assert body["name"] == name
    return response, body

def patch_update_user_job(api_url, headers, job, user_id="2"):
    response = requests.patch(api_url + f"/api/users/{user_id}", headers=headers, data={"job": job})
    body = response.json()
    assert body["job"] == job
    return response, body

# DELETE
def delete_user(api_url, headers, user_id="2"):
    response = requests.delete(api_url + f"/api/users/{user_id}", headers=headers)
    return response


def check_response_code(response, code):
    assert response.status_code == code


def check_response_schema(body, schema):
    validate(body, schema=schema)

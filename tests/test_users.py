import src.schema

import src.api.users
import src.schema.users_schema


users = src.api.users
schema = src.schema.users_schema

# GET
def test_get_users(api_url, headers):
    response = users.get_users(api_url, headers)
    users.check_response_code(response, 200)


def test_get_non_existent_user(api_url, headers):
    response = users.get_non_existent_users(api_url, headers)
    users.check_response_code(response, 404)


def test_get_unknown_methode(api_url, headers):
    response = users.get_unknown_methode(api_url, headers)
    users.check_response_code(response, 404)


def test_get_broken_uri_methode(api_url, headers):
    response = users.get_incomplete_url(api_url, headers)
    users.check_response_code(response, 404)


# POST
def test_create_user(api_url, headers):
    response, body = users.post_users_should_be_create(api_url, headers, 'morpheus', 'master')
    users.check_response_code(response, 201)
    users.check_response_schema(body, schema.post_users)


def test_create_user_without_data(api_url, headers):
    response = users.post_create_users_data_empty(api_url, headers)
    users.check_response_code(response, 201)


def test_creat_user_fails_without_api_key(api_url):
    response = users.post_verify_users_creation_fails(api_url)
    users.check_response_code(response, 401)


# PUT
def test_user_put_should_be_update(api_url,headers):
    response, body = users.put_update_users(api_url, headers, 'morpheus', 'test')
    users.check_response_code(response, 200)
    users.check_response_schema(body, schema.put_schema)


# PATCH
def test_user_name_should_be_update(api_url,headers):
    response, body = users.patch_update_user_name(api_url, headers, 'testtest')
    users.check_response_code(response, 200)
    users.check_response_schema(body, schema.patch_user_name_schema)


def test_user_job_should_be_update(api_url,headers):
    response, body = users.patch_update_user_job(api_url, headers, 'qa')
    users.check_response_code(response, 200)
    users.check_response_schema(body, schema.patch_user_job_schema)

# DELETE
def test_delete_user(api_url,headers):
     response = users.delete_user(api_url, headers)
     users.check_response_code(response, 204)
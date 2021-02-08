import requests
import json
import jsonpath
import pytest

@pytest.fixture(scope = 'module')
def sendPostRequestToCreateUser():
    global url, response, status
    url = 'https://reqres.in/api/users'
    file = open('C:\\Users\\HP\\Desktop\\API\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)

@pytest.mark.Smoke
def test_create_new_user(sendPostRequestToCreateUser):
    assert response.status_code == 201

@pytest.mark.skip
def test_get_id_of_new_user(sendPostRequestToCreateUser):
    response_json = json.loads(response.text)
    newResourseId = jsonpath.jsonpath(response_json, 'id')
    assert newResourseId == '123'
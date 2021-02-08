import json
import requests
import jsonpath
import pytest

@pytest.mark.oAuthCheck
def test_add_new_student():
    global id
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')

@pytest.mark.oAuthCheck
def test_oauth_api():
    token_url = 'http://thetestingworldapi.com/api/Token'
    data = {'grant_type':'password', 'username':'admin', 'password':'Hz_Che_Tut'}
    t_response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(t_response.json(), 'access_token')
    access_token = token_value[0]
    auth = {'Authorization':'Bearer: '+access_token}
    API_URL_DETAIL = 'http://thetestingworldapi.com/api/StDetails/' + str(id[0])
    response = requests.get(API_URL_DETAIL, headers=auth)
    print(response.text)
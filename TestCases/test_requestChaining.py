import requests
import json
import jsonpath
import pytest

@pytest.mark.Chaining
def test_add_new_student():
    global id
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

@pytest.mark.Chaining
def test_get_student_detail():
    API_URL_DETAIL = 'http://thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    response = requests.get(API_URL_DETAIL)
    print(response.text)
    print(response.url)
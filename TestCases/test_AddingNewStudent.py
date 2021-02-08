import json
import jsonpath
import requests


def test_add_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(API_URL, request_json)
    print(response.text)

def test_get_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails/75386'
    response = requests.get(API_URL)
    print(response.text)
    json_response = json.loads(response.text)
    first_name = jsonpath.jsonpath(json_response, 'data.first_name')
    assert first_name[0] == 'Hard'

def test_update_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails/75386'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(API_URL, request_json)
    response_json = json.loads(response.text)
    middle_name = jsonpath.jsonpath(response_json, 'middle_name')
    print(response.text)
    print(middle_name)
    assert middle_name[0] == 'Auto Testing'
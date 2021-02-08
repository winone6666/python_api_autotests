import requests
import json
import jsonpath

def test_add_new_data():
    global id
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    TECH_API_URL = 'http://thetestingworldapi.com/api/technicalskills'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\TechDetails.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(TECH_API_URL, request_json)
    print(response.text)

    ADDRESS_API_URL = 'http://thetestingworldapi.com/api/addresses'
    request_json_input = open('C:\\Users\\HP\\Desktop\\API\\AddressRequest.json', 'r')
    request_json = json.loads(request_json_input.read())
    response = requests.post(ADDRESS_API_URL, request_json)
    print(response.text)

    FINAL_DETAIL_URL = 'http://thetestingworldapi.com/api/finalstudentdetails/'+str(id[0])
    response = requests.get(FINAL_DETAIL_URL)
    print(response.content)
    print(response.url)
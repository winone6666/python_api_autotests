import requests
import json
import jsonpath
import pytest

@pytest.mark.Smoke
def test_fetch_user_data():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    json_response = json.loads(response.text)
    for i in range(0, 3):
        email = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].email')
        print(email[0])
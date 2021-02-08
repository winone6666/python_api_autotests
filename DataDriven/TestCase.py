import json
import requests

from DataDriven import Library


def test_create_students_from_excel1():
    # API
    url = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\HP\\Desktop\\API\\RequestJson.json', 'r')
    json_request = json.loads(file.read())

    obj = Library.Common('C:\\Users\\HP\\Desktop\\API\\students_data.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_name()

    # Excel Code
    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(url, updated_json_request)
        print(response.text)

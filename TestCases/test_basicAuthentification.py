import requests
from requests.auth import HTTPBasicAuth

def test_with_auth():
    response = requests.get('https://github.com/user', auth=HTTPBasicAuth('winone6666@yandex.ru', '12345678'))
    print(response.text)
import json
import os
import urllib.parse

import requests


requests_session = requests.Session()
requests_session.url = 'https://jsonplaceholder.typicode.com'
requests_session.verify = False
requests_session.headers.update({'Content-Type': 'application/json'})


def get_json_schema(request=None, file_name=None):
    assert request or file_name, 'request or file_name required'
    if request:
        path = urllib.parse.urlparse(request.path_url).path
        file_name = f'{request.method}{path.replace("/", "_")}.json'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'json_schemas/{file_name}')
    with open(file_path, 'r') as f:
        json_schema = json.load(f)
    return json_schema

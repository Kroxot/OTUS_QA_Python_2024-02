from jsonschema import validate

from homework_5.open_brewery_api_service import get_json_schema, requests_session


def test_get_random_brewery():
    response = requests_session.get(f"{requests_session.url}/random")
    assert response.status_code == 200
    assert response.json()
    validate(instance=response.json(), schema=get_json_schema(response.request))

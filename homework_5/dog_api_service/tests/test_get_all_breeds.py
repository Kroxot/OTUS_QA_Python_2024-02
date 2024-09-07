from jsonschema import validate

from homework_5.dog_api_service import get_json_schema, requests_session


def test_get_all_breeds():
    response = requests_session.get(f"{requests_session.url}/breeds/list/all")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_json_schema(response.request))
    assert response.json()["status"] == "success"

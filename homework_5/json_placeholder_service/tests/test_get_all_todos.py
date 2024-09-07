from jsonschema import validate

from homework_5.json_placeholder_service import get_json_schema, requests_session


def test_get_all_users():
    response = requests_session.get(f"{requests_session.url}/todos")
    assert response.status_code == 200
    assert response.json()
    validate(instance=response.json(), schema=get_json_schema(response.request))

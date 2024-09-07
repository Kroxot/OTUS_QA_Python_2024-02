from jsonschema import validate

from homework_5.open_brewery_api_service import get_json_schema, requests_session


def test_get_all_breweries():
    response = requests_session.get(f"{requests_session.url}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_json_schema(response.request))
    assert len(response.json()) > 0

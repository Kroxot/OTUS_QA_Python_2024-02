import pytest
from jsonschema import validate

from homework_5.open_brewery_api_service import get_json_schema, requests_session


@pytest.mark.parametrize("city", ["San Diego", "Norman"])
def test_get_breweries_by_city(city):
    response = requests_session.get(url=requests_session.url, params={"by_city": city})
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_json_schema(response.request))
    assert len(response.json()) > 0
    for brewery in response.json():
        assert brewery["city"] == city

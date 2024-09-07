import pytest
from jsonschema import validate

from homework_5.dog_api_service import get_json_schema, requests_session


@pytest.mark.parametrize("breed", ["hound", "poodle", "setter"])
def test_get_all_breeds(breed):
    response = requests_session.get(f"{requests_session.url}/breed/{breed}/list")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_json_schema(file_name='GET_api_breed_breed_list.json'))
    assert len(response.json()["message"]) > 0
    assert response.json()["status"] == "success"

import pytest
from jsonschema import validate

from homework_5.dog_api_service import requests_session, get_json_schema


@pytest.mark.parametrize("breed", ["akita", "beagle", "boxer"])
def test_get_breed_images(breed):
    response = requests_session.get(f"{requests_session.url}/breed/{breed}/images/random")
    assert response.status_code == 200
    validate(instance=response.json(), schema=get_json_schema(file_name='GET_api_breed_breed_images_random.json'))
    assert response.json()["status"] == "success"
    assert response.json()["message"].endswith(".jpg")

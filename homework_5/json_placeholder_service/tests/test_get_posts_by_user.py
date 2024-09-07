import pytest
from jsonschema import validate

from homework_5.json_placeholder_service import get_json_schema, requests_session


@pytest.mark.parametrize('user_id', [1, 2, 10])
def test_get_posts_by_user(user_id):
    response = requests_session.get(f"{requests_session.url}/posts", params={'userId': user_id})
    assert len(response.json()) > 0
    validate(instance=response.json(), schema=get_json_schema(response.request))
    for post in response.json():
        assert post['userId'] == user_id

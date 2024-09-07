import pytest
from jsonschema import validate

from homework_5.json_placeholder_service import get_json_schema, requests_session


@pytest.mark.parametrize('post_id', [3, 4, 11])
def test_get_posts_by_user(post_id):
    response = requests_session.get(f"{requests_session.url}/comments", params={'postId': post_id})
    assert len(response.json()) > 0
    validate(instance=response.json(), schema=get_json_schema(response.request))
    for comment in response.json():
        assert comment['postId'] == post_id

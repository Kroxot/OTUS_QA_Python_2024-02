from jsonschema import validate

from homework_5.json_placeholder_service import get_json_schema, requests_session


def test_post_create_user():
    body = {
        "name": "Андрейка Назаров",
        "username": "Kroxotb",
        "email": "kroxotb@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "Тамбов",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
        },
        "phone": "1-463-123-4447",
        "website": "kroxotb.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
        }
    }
    response = requests_session.post(f"{requests_session.url}/users", json=body)
    assert response.status_code == 201
    assert response.json()
    validate(instance=response.json(), schema=get_json_schema(response.request))
    assert response.json()['id'] == 11
    assert response.json()['name'] == 'Андрейка Назаров'
    assert response.json()['username'] == 'Kroxotb'
    assert response.json()['email'] == 'kroxotb@yesenia.net'
    assert response.json()['phone'] == '1-463-123-4447'
    assert response.json()['website'] == 'kroxotb.info'
    assert response.json()['address']['street'] == 'Douglas Extension'
    assert response.json()['address']['suite'] == 'Suite 847'
    assert response.json()['address']['city'] == 'Тамбов'
    assert response.json()['address']['zipcode'] == '59590-4157'
    assert response.json()['address']['geo']['lat'] == '-68.6102'
    assert response.json()['address']['geo']['lng'] == '-47.0653'
    assert response.json()['company']['name'] == 'Romaguera-Jacobson'
    assert response.json()['company']['catchPhrase'] == 'Face to face bifurcated interface'
    assert response.json()['company']['bs'] == 'e-enable strategic applications'

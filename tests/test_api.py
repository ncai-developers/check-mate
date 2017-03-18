import api
import requests_mock

def test_get_data():
    user_id = "017770"
    expected_json = {
        "name":"",
        "balance":20,
        "photo":"",
        "id":"017770"
    }
    with requests_mock.Mocker() as mock:
        # mock get request to api url
        mock.get(api.api_url + user_id, json=expected_json)
        json = api.get_data(user_id)
        assert type(json["name"]) is str
        assert type(json["balance"]) is int
        assert type(json["photo"]) is str
        assert type(json["id"]) is str

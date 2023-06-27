import requests


def post_1c(uri: str, login: str, password: str, club_id: str):
    _params = {
        "Request_id": "e1477272-88d1-4acc-8e03-7008cdedc81e",
        "ClubId": club_id,
        "Method": "GetSpecialistList",
        "Parameters": {
            "ServiceId": "1"
        }
    }

    with requests.Session() as s:
        s.auth = (login, password)

        response = s.post(uri, json=_params)
    return response

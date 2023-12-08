import requests


def test_get_repos():
    response = requests.get(f"http://0.0.0.0:7000/api/repos")
    assert response.status_code == 200


def test_get_repos_language():
    response = requests.get(f"http://0.0.0.0:7000/api/repos/python")
    assert response.status_code == 200
    response = response.json()
    assert response['data'][0]['language'] == "Python"
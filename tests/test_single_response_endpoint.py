import requests

from helpers.api_helper import make_request_and_get_status
from helpers.end_points import single_article_url


def test_get_request_is_successful():
    response = requests.get(url=single_article_url)
    assert response.headers.get('content-type') == 'application/json'
    assert response.status_code == 200, f"Incorrect status code received: {status_code_received}"


def test_post_request_is_unsuccessful():
    response = requests.post(url=single_article_url)
    status_code_received = response.status_code
    assert response.headers.get('content-type') == 'application/json'
    assert response.status_code == 404, f"Incorrect status code received: {status_code_received}"


def test_put_request_is_unsuccessful():
    response = requests.put(url=single_article_url)
    assert response.headers.get('content-type') == 'application/json'
    assert response.status_code == 404


def test_delete_request_is_unsuccessful():
    response = requests.delete(url=single_article_url)
    assert response.headers.get('content-type') == 'application/json'
    assert response.status_code == 404

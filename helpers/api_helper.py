import requests

from helpers.end_points import single_article_url, multiple_article_url


def verify_if_response_type_is_json(response):
    assert response.headers.get('content-type') == 'application/json'


def verify_resp_type_status_code(method, url):
    response = requests.request(method=method, url=url)
    verify_if_response_type_is_json(response)
    assert response.status_code == get_correct_status_code(method), \
        f"Following Incorrect status code received: {response.status_code}"


def verify_no_of_total_articles_received(url):
    response_in_dict = requests.get(url=url).json()
    if url == single_article_url:
        assert len(response_in_dict) > 1, f"Unexpected no of articles: {len(response_in_dict)}"
    elif url == multiple_article_url:
        assert len(response_in_dict) > 1, f"Unexpected no of articles: {len(response_in_dict)}"
    else:
        raise Exception('Incorrect url entered')


def get_correct_status_code(method):
    if method == 'GET':
        return 200
    elif method == 'POST' or 'PUT' or 'DELETE':
        return 404
    else:
        raise Exception('Incorrect request method entered.')

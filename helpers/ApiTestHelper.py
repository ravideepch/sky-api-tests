import requests

from helpers.end_points import single_article_url, multiple_article_url


def verify_if_response_type_is_json(response):
    assert response.headers.get('content-type') == 'application/json'


def get_correct_status_code(method):
    if method == 'GET':
        return 200
    elif method == 'POST' or 'PUT' or 'DELETE':
        return 404
    else:
        raise Exception('Incorrect request method entered.')


class ApiTestHelper:
    def __init__(self, url):
        self.url = url

    def verify_resp_type_status_code(self, method):
        response = requests.request(method=method, url=self.url)
        verify_if_response_type_is_json(response)
        assert response.status_code == get_correct_status_code(method), \
            f"Following Incorrect status code received: {response.status_code}"

    def verify_no_of_total_articles_received(self):
        response_in_dict = requests.get(url=self.url).json()
        if self.url == single_article_url:
            assert 'id' in response_in_dict
        elif self.url == multiple_article_url:
            assert len(response_in_dict) > 1, f"Unexpected no of articles: {len(response_in_dict)}"
        else:
            raise Exception('Incorrect url entered')
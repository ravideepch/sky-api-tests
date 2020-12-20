import requests

from helpers.api_helper import verify_resp_type_status_code, verify_no_of_total_articles_received
from helpers.end_points import single_article_url
from jsonschema import validate, ValidationError, SchemaError


def test_get_request_is_successful():
    verify_resp_type_status_code('GET', single_article_url)


def test_post_request_is_unsuccessful():
    verify_resp_type_status_code('POST', single_article_url)


def test_put_request_is_unsuccessful():
    verify_resp_type_status_code('PUT', single_article_url)


def test_delete_request_is_unsuccessful():
    verify_resp_type_status_code('DELETE', single_article_url)


def test_no_of_total_articles_received():
    print(requests.get(url=single_article_url).text)
    verify_no_of_total_articles_received(single_article_url)
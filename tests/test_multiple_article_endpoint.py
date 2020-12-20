from helpers.api_helper import verify_resp_type_status_code, verify_no_of_total_articles_received
from helpers.end_points import multiple_article_url


def test_get_request_is_successful():
    verify_resp_type_status_code('GET', multiple_article_url)


def test_post_request_is_unsuccessful():
    verify_resp_type_status_code('POST', multiple_article_url)


def test_put_request_is_unsuccessful():
    verify_resp_type_status_code('PUT', multiple_article_url)


def test_delete_request_is_unsuccessful():
    verify_resp_type_status_code('DELETE', multiple_article_url)


def test_no_of_total_articles_received():
    verify_no_of_total_articles_received(multiple_article_url)

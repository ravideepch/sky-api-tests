import pytest

from helpers.ApiTestHelper import ApiTestHelper
from helpers.end_points import single_article_url


@pytest.fixture()
def setup():
    api_test = ApiTestHelper(single_article_url)
    yield api_test


class TestSingleArticle:
    def test_get_request_is_successful(self, setup):
        setup.verify_resp_type_status_code('GET')

    def test_post_request_is_unsuccessful(self, setup):
        setup.verify_resp_type_status_code('POST')

    def test_put_request_is_unsuccessful(self, setup):
        setup.verify_resp_type_status_code('PUT')

    def test_delete_request_is_unsuccessful(self, setup):
        setup.verify_resp_type_status_code('DELETE')

    def test_no_of_total_articles_received(self, setup):
        setup.verify_no_of_total_articles_received()

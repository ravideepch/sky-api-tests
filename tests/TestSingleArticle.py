import pytest

from helpers.ApiTestHelper import ApiTestHelper
from helpers.end_points import single_article_url


@pytest.fixture()
def init():
    api_test = ApiTestHelper(single_article_url)
    yield api_test


class TestSingleArticle:

    def test_get_request_is_successful(self, init):
        init.verify_resp_type_status_code('GET')

    def test_post_request_is_unsuccessful():
        init.verify_resp_type_status_code('POST', single_article_url)


    def test_put_request_is_unsuccessful():
        init.verify_resp_type_status_code('PUT', single_article_url)


    def test_delete_request_is_unsuccessful():
        init.verify_resp_type_status_code('DELETE', single_article_url)


    def test_no_of_total_articles_received():
        print(requests.get(url=single_article_url).text)
        init.verify_no_of_total_articles_received(single_article_url)
from pages.login_page import AuthorizationPage
import pytest

email = "qa1@fusion.ru"
code = "654321"
@pytest.mark.login
def test_01_authorization(browser):
    auth_page = AuthorizationPage(browser)
    auth_page.email_field(email)
    auth_page.submit_button()
    auth_page.one_time_code(code)
    auth_page.enter_space_button()
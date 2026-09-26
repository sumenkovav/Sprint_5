import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import LogoutLocators


class TestLogout:
    def test_logout_from_personal_account(self, authorized_main_page):  # проверяем выход по кнопке «Выйти»
        authorized_main_page.find_element(*LogoutLocators.PERSONAL_ACCOUNT_LINK).click()   # нажимаем личный кабинет
        authorized_main_page.find_element(*LogoutLocators.LOGOUT_BUTTON).click()            # нажимаем выход

        wait = WebDriverWait(authorized_main_page, 5)
        wait.until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
        assert authorized_main_page.current_url == "https://stellarburgers.education-services.ru/login"
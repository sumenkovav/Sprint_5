import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import LoginAccountLocators
from tests.test_data import VALID_USER

class TestFromPersonalAccountToConstruktor:

    def test_from_personal_account_to_construktor(self, main_page):
        
        main_page.find_element(*LoginAccountLocators.PERSONAL_ACCOUNT_LINK).click() # нажимаем на кнопку "Личный Кабинет" на главной
        
        main_page.find_element(*LoginAccountLocators.EMAIL_INPUT_LOGIN).send_keys(VALID_USER["email"]) # вводим E-mail
        
        main_page.find_element(*LoginAccountLocators.INP_PAS).send_keys(VALID_USER["password"]) # вводим пароль
        
        main_page.find_element(*LoginAccountLocators.SUBMIT_LOGIN).click() # нажимаем кнопку "Войти"
        
        # ожидаем появления кнопки "Оформить заказ".
        wait = WebDriverWait(main_page, 5)
        order_button = wait.until(EC.visibility_of_element_located(LoginAccountLocators.TITLE_ORDER))
        assert order_button.is_displayed()
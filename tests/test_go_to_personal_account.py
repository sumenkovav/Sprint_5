import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import LoginAccountLocators
from tests.test_data import VALID_USER

class TestGoToPersonalAccount:
    def test_go_to_personal_account(self, main_page):

# нажимаем на кнопку "Личный Кабинет" на главной
        main_page.find_element(*LoginAccountLocators.PERSONAL_ACCOUNT_LINK).click()

# вводим E-mail       
        main_page.find_element(*LoginAccountLocators.EMAIL_INPUT_LOGIN).send_keys(VALID_USER["email"])

# вводим пароль        
        main_page.find_element(*LoginAccountLocators.INP_PAS).send_keys(VALID_USER["password"])

# нажимаем кнопку "Войти"        
        main_page.find_element(*LoginAccountLocators.SUBMIT_LOGIN).click() 
        
# ожидаем появления кнопки "Оформить заказ".
        wait = WebDriverWait(main_page, 5)
        order_button = wait.until(EC.visibility_of_element_located(LoginAccountLocators.TITLE_ORDER))
        assert order_button.is_displayed()
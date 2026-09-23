import pytest
from tests.locators import RegistrationLocators



class TestRegistration:
    def test_registration_success(self, main_page, valid_user):

        main_page.find_element(*RegistrationLocators.BUTTON_ENTER).click() # нажимаем кнопку войти в аккаунт

        main_page.find_element(*RegistrationLocators.REGISTER_LINK).click() # нажимаем ссылку на регистрацию

    #заполняем поля
        main_page.find_element(*RegistrationLocators.NAME_FIELD).send_keys(valid_user["name"])    #поле имя 
        main_page.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(valid_user["email"])   #поле емайл
        main_page.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(valid_user["password"]) #поле пароль  

        main_page.find_element(*RegistrationLocators.BUTTON_CHEKIN).click() # нажимаем кнопку зарегистрироваться

        assert main_page.find_element(*RegistrationLocators.TITLE_LOGIN).is_displayed() #ожидаем вывод на экран кнопки "Войти"

# негативный тест с невалидным паролем

    def test_registration_invalid_password(self, main_page, valid_user):

        valid_user["password"] = "123" 

        main_page.find_element(*RegistrationLocators.BUTTON_ENTER).click() # нажимаем кнопку войти в аккаунт

        main_page.find_element(*RegistrationLocators.REGISTER_LINK).click() # нажимаем ссылку на регистрацию

    #заполняем поля
        main_page.find_element(*RegistrationLocators.NAME_FIELD).send_keys(valid_user["name"])    #поле имя 
        main_page.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(valid_user["email"])   #поле емайл
        main_page.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(valid_user["password"]) #поле пароль 

        main_page.find_element(*RegistrationLocators.BUTTON_CHEKIN).click() # нажимаем кнопку зарегистрироваться

        error_message = main_page.find_element(*RegistrationLocators.MESSAGE_ERROR)  # проверяем вывод сообщения об ошибке
        assert error_message.is_displayed()   
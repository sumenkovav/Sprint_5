import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_data import VALID_USER


#создаёт экземпляр Chrome-драйвера
@pytest.fixture  
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# генерация валидных данных пользователя
def generate_unique_email():
    #Генерирует уникальный email для регистрации
    prefix = "sumenkov_55kogorta"
    random_number = random.randint(100, 999)
    return f"{prefix}{random_number}@yandex.ru"

@pytest.fixture
def valid_user():
    # Фикстура больше не делает сложную математику, она просто собирает данные
    return {
        "name": "Александр",
        "email": generate_unique_email(),  # Вызываем нашу функцию
        "password": "123456"
    } 
 


# открытие главной страницы
@pytest.fixture
def main_page(driver: WebDriver):
    url = "https://stellarburgers.education-services.ru/"
    driver.get(url)
    return driver


# авторизация.
@pytest.fixture 
def authorized_main_page(main_page: WebDriver):
    main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    main_page.find_element(By.XPATH, "(//input[@name='name'])").send_keys(VALID_USER["email"])
    main_page.find_element(By.NAME, "Пароль").send_keys(VALID_USER["password"])
    main_page.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(main_page, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
    return main_page
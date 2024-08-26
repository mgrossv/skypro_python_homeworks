import allure
import pytest
from selenium import webdriver
from FormPage import FormPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.id("PersonalData")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.story("Заполнение персональных данных")
@allure.feature("CREATE")
@allure.title("Заполнить персональные данные")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
def test_fill_form_and_check_validation(browser):
    with allure.step("Открыть страницу веб-браузера"):
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    with allure.step("Создание переменной,"
                     "которая хранит экзампляр класса PersonalDataPage"):
        form_page = FormPage(browser)

    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
                        "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    form_page.other_fields_green()
    form_page.zip_code_red()

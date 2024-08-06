import pytest
from selenium import webdriver
from Form.FormPage import FormPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_form_and_check_validation(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(browser)

    # Данные для заполнения формы
    data = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone_number": "+7 985 899 99 87",
        "city": "Москва",
        "country": "Россия",
        "job_position": "QA",
        "company": "SkyPro"
    }

    # Заполнение формы
    form_page.fill_form(data)
    # Проверка цвета
    form_page.other_fields_green()
    form_page.zip_code_red()
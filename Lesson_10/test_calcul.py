import allure
import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.id("Calculator")
@allure.epic("калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_form_calculator():
    with allure.step("Открытие страницы в веб-браузере"):
        driver = webdriver.Chrome()
    with allure.step("Создание переменной,"
                     "которая хранит экземпляр класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    calculator_page.delay()
    to_be = calculator_page.sum_of_the_numbers()
    wait_result = calculator_page.get_result()

    assert wait_result == to_be

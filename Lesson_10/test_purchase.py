import allure
from selenium import webdriver
from PurPage import PurPage


@allure.id("Internet_mag")
@allure.epic("Интернет магазин")
@allure.severity("blocker")
@allure.story("Покупка товаров")
@allure.feature("CREATE")
@allure.title("Выбор товара, работа с корзиной и оплата")
@allure.suite("Тесты на работу с интернет-магазином")
def test_purpage():
    with allure.step("Открытие страницы веб-браузера"):
        driver = webdriver.Chrome()
    with allure.step("Создание переменной,"
                     " которая хранит экзампляр класса InternetMagPage"):
        pur_page = PurPage(driver)

    price = pur_page.autorization()
    pur_page.add()
    pur_page.shopping_cart_and_checkout()
    pur_page.form_of_payment()
    total_price = pur_page.total_price()
    with allure.step("Проверить,что ожидаемая и фактическая стоимость равны"):
        assert price == total_price

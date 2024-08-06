from selenium import webdriver
from Purchase.PurPage import PurPage


def test_purpage():
    driver = webdriver.Chrome()
    pur_page = PurPage(driver)

    price = pur_page.autorization()
    pur_page.add()
    pur_page.shopping_cart_and_checkout()
    pur_page.form_of_payment()
    total_price = pur_page.total_price()

    assert price == total_price
    
import allure
from selenium.webdriver.common.by import By


class PurPage:
    """"Этот класс пердставляет страницу веб-магазина.
    Авторизованный пользователь может выбрать вещи,
    посомтреть окончательную сумму покупки и оплатить ее"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(5)

    @allure.step("Авторизуйтесь как пользователь")
    def autorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    
    @allure.step("Переход в корзину и оформление покупки")
    def shopping_cart_and_checkout(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()
    
    @allure.step("Заполнение формы оплаты")
    def form_of_payment(self):
        self.driver.find_element(By.ID, "first-name").send_keys('Maria')
        self.driver.find_element(By.ID, "last-name").send_keys('Gross')
        self.driver.find_element(By.ID, "postal-code").send_keys('144661')
        self.driver.find_element(By.ID, "continue").click()
    
    @allure.step("Окончательная сумма покупок")
    def total_price(self):
        self.driver.find_element(By.CLASS_NAME, "summary_total_label").get_attribute("textContent")
    
    @allure.step("Закрытие браузера")
    def close(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#finish").click()
        self.driver.quit()
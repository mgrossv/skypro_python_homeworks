from selenium.webdriver.common.by import By


class PurPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(5)

    # Авторизуйтесь как пользователь
    def autorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    # Добавьте в корзину товары
    def add(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Перейдите в корзину и нажмите Checkout
    def shopping_cart_and_checkout(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

    # Заполните форму своими данными
    def form_of_payment(self):
        self.driver.find_element(By.ID, "first-name").send_keys('Maria')
        self.driver.find_element(By.ID, "last-name").send_keys('Gross')
        self.driver.find_element(By.ID, "postal-code").send_keys('144661')
        self.driver.find_element(By.ID, "continue").click()

    # Прочтите со страницы итоговую стоимость
    def total_price(self):
        self.driver.find_element(By.CLASS_NAME, "summary_total_label").get_attribute("textContent")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
    def delay(self):
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys('45')

    # Сумма чисел
    def sum_of_the_numbers(self):
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"7")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"8")]').click()
        self._driver.find_element(
            By.XPATH, '//span[contains(text(),"=")]').click()

    # Результат
    def get_result(self):
        WebDriverWait(self._driver, "46").until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        self._driver.find_element(By.CLASS_NAME, "screen").text

    def close_driver(self):
        self._driver.quit()
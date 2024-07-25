from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.labirint.ru/")
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Python")

sleep(10)
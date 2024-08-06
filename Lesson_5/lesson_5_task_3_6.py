from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/login")
    firefox.get("http://the-internet.herokuapp.com/login")
    # В поле username введите значение tomsmith
    input_name = chrome.find_element(By.ID, "username").send_keys("tomsmith")
    input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(3)
    # В поле password введите значение SuperSecretPassword!
    input_pass = chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    input_pass = firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(3)
    # Нажмите кнопку Login
    button = chrome.find_element(By.TAG_NAME, "button").click()
    button = firefox.find_element(By.TAG_NAME, "button").click()
    sleep(3)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()
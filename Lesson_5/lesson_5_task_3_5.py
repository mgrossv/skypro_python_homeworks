from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/inputs")
    firefox.get("http://the-internet.herokuapp.com/inputs")

    input_field = chrome.find_element(By.TAG_NAME, "input")
    input_field = firefox.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(3)
    input_field.clear()
    sleep(1)
    input_field.send_keys(999)
    sleep(3)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()
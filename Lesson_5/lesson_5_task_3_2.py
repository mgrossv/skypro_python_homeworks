from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")
    # Кликните на синюю кнопку 
    blue_button = chrome.find.element(
        "xpath", '//button[text()="Button with Dinamic ID"]').click()
    blue_button = firefox.find.element(
        "xpath", '//button[text()="Button with Dinamic ID"]').click()
    
    # Кликните на синюю кнопку три раза подряд
    for a in range(3):
        blue_button = chrome.find.element(
        "xpath", '//button[text()="Button with Dinamic ID"]').click()
        blue_button = firefox.find.element(
        "xpath", '//button[text()="Button with Dinamic ID"]').click()
        count = count + 1
        sleep(3)
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()
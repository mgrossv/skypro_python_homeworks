import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    
    wait = WebdriverWait(chrome, 10)
    wait = WebdriverWait(firefox, 10)

    close_button = wait.until(EC.element_to_be_clickabel(
        (By.CSS_SELECTOR,".modal-footer")))
    time.sleep(5)
    # В модальном окне нажмите на кнопку Сlose
    close_button.click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()
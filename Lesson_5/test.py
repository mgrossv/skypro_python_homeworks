from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://www.google.com')
print(driver.title)
driver.quit()
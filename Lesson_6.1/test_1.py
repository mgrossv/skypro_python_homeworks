from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import *
from time sleep


def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    form_data = {
    "first-name": first_name,
    "last-name": last_name, 
    "address": address,
    "email": email,
    "phone-number": phone_number,
    "zip-code": zip_code,
    "city": city,
    "country": country, 
    "job-position": job_position, 
    "company": company
    }

    for field_name, value in form_data.items():
        chrome_browser.find.element(By.NAME, field_name).send_keys(value)

    WebdriverWait(chrome_browser,40, 0.1).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(3)

    field_classes = {
        "first-name":"success",
        "last-name": "success", 
        "address": "success",
        "email": "success",
        "phone-number": "success",
        "zip-code": "danger",
        "city": "success",
        "country": "success", 
        "job-position": "success", 
        "company": "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in chrome_browser.find_element(
            By.ID, field_id).get_attribute("class")
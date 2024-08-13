from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.first_name = (By.NAME, "first-name")
        self.last_name = (By.NAME, "last-name")
        self.address = (By.NAME, "address")
        self.email = (By.NAME, "e-mail")
        self.phone_number = (By.NAME, "phone")
        self.city = (By.NAME, "city")
        self.country = (By.NAME, "country")
        self.job_position = (By.NAME, "job-position")
        self.company = (By.NAME, "company")
        self.submit_button = (By.CLASS_NAME, "btn.btn-outline-primary")
        self.zip_code = (By.CSS_SELECTOR, "#zip-code")

    def fill_form(self, data):
        self.driver.find_element(*self.first_name).send_keys(data['first_name'])
        self.driver.find_element(*self.last_name).send_keys(data['last_name'])
        self.driver.find_element(*self.address).send_keys(data['address'])
        self.driver.find_element(*self.email).send_keys(data['email'])
        self.driver.find_element(*self.phone_number).send_keys(data['phone_number'])
        self.driver.find_element(*self.city).send_keys(data['city'])
        self.driver.find_element(*self.country).send_keys(data['country'])
        self.driver.find_element(*self.job_position).send_keys(data['job_position'])
        self.driver.find_element(*self.company).send_keys(data['company'])
        self.driver.find_element(*self.submit_button).click()

    # Проверьте (assert), что поле Zip code подсвечено красным.
    def zip_code_red(self):
        zip_code_color = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color == 'rgba(248, 215, 218, 1)'

    # Проверьте (assert), что остальные поля подсвечены зеленым
    def other_fields_green(self):
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position",
                        "#company"]
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
        return field_color == 'rgba(209, 231, 221, 1)'
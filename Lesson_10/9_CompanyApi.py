import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url

    @allure.step('Получить токен авторизации с помощью API')
    def get_token(self, user="flora", password="nature-fairy"):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(f'{self.url}/auth/login', json=creds)
        token = resp.json()["userToken"]
        return token
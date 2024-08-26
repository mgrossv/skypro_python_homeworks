import allure
from EmployeeApi import EmployeeApi
from CompanyTable import CompanyTable
from EmployeesTable import EmployeeTable


base_url = 'https://x-clients-be.onrender.com'
employee_api = EmployeeApi(base_url)

db_connection_string = (
    "postgresql://x_clients_user:"
    "95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa"
    "@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/"
    "x_clients_db_fxd0")
company_table = CompanyTable(db_connection_string)
employee_table = EmployeeTable(db_connection_string)

# Новая компания
name = 'Новая компания'
description = 'Совсем новая'

# Новый сотрудник
id = 1
first_name = "Иван"
last_name = "Иванов"
middle_name = "Иванович"
email = "ivan@gmail.com"
employee_url = "url1.com"
phone = "+70002225566"
birthdate = "2011-07-07T08:06:30.137Z"
is_active = True


@allure.title('Получить список сотрудников')
@allure.description('Тест получения списка сотрудников с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee_list():
    # Cоздать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # Cоздать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # Получить список сотрудников с помощью API
    employee_list_api = employee_api.get_employee_list(new_company_id)

    # Получить список сотрудников в DB
    employee_list_db = employee_table.get_company_employees(new_company_id)

    # Удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee_list_api[0]["id"] == new_employee_id, \
        "Employee's ID is not equal"
    assert len(employee_list_api) == len(employee_list_db)


@allure.title('Создать сотрудника')
@allure.description('Тест создания сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee():
    # Создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # Создать нового сотрудника с помощью API
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, new_company_id,
                                             email, employee_url, phone,
                                             birthdate, is_active)
    new_employee_id = new_employee["id"]

    # Получить сотрудника из DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # Удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert len(employee) == 1, "Employee was not created"


@allure.title('Получить сотрудника')
@allure.description('Протестируйте сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_get_employee():
    # Создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # Создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # Получите информацию о сотруднике с помощью API
    employee = employee_api.get_employee(new_employee_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee["id"] == new_employee_id
    assert employee["firstName"] == first_name
    assert len(employee) == 12


@allure.title('Сменить сотрудника с помощью API')
@allure.description('Протестируйте смену сотрудника с помощью API')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_api():
    # Создатиь новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # Создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # Изменить сотрудника с помощью API
    new_email = "new_ivan@gmail.com"
    new_url = "url7.com"
    new_is_active = False
    patched_employee = employee_api.patch_employee(new_employee_id,
                                                   new_email,
                                                   new_url, new_is_active)
    assert patched_employee["id"] == new_employee_id
    assert patched_employee["email"] == new_email
    assert patched_employee["url"] == new_url
    assert patched_employee["isActive"] == new_is_active

    # Получите исправленную информацию о сотруднике из DB
    employee = employee_table.get_employee_by_id(new_employee_id)

    # Удалить нового сотрудника и новую компанию из DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    with allure.step('Проверьте исправленную информацию о сотруднике из DB'):

        assert employee[0][8] == new_email
        assert employee[0][10] == new_url
        assert employee[0][1] == new_is_active


@allure.title('Изменить сотрудника по DB')
@allure.description('Тестовое изменение сотрудника по DB')
@allure.feature('Сотрудник')
@allure.severity(allure.severity_level.NORMAL)
def test_change_employee_by_db():
    # Создать новую компанию в DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # Создать нового сотрудника в DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # Изменить сотрудника с помощью DB
    new_email = "new_ivan@gmail.com"
    new_url = "url7.com"
    new_is_active = False
    employee_table.update(new_employee_id, new_email, new_url, new_is_active)

    # Получите информацию о сотруднике с помощью API
    employee = employee_api.get_employee(new_employee_id)

    with allure.step('Проверьте исправленную информацию о сотруднике из API'):

        assert employee["id"] == new_employee_id
        assert employee["email"] == new_email
        assert employee["avatar_url"] == new_url
        assert employee["isActive"] == new_is_active

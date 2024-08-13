from test_API import API

api = API("https://x-clients-be.onrender.com")


def test_add_new_employee():
    # Создать новую компанию

    name = "Новая компания"
    descr = "Компашка"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # Получить список сотрудников
    body = api.get_employees_list(companyId)
    len_before = len(body)

    # добавить нового сотрудника
    firstName = "Иван"
    lastName = "Иванов"
    middleName = "Иванович"
    email = "ivan@mail.ru"
    url = "string"
    phone = "899423000066"
    birthdate = "2000-08-13"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone, birthdate,
                                       isActive)
    emp_id = new_employee["id"]

    # Получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Иван"
    assert body[-1]["lastName"] == "Иванов"
    assert body[-1]["middleName"] == "Иванович"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "899423000066"
    assert body[-1]["birthdate"] == "2000-08-13"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id


def test_get_employees_id():
    # Создать новую компанию
    name = "Компания NEW"
    descr = "Компания"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']

    # Получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    begin_list = len(body)

    # Добавить нового сотрудника
    firstName = "Петр"
    lastName = "Петров"
    middleName = "Петрович"
    email = "pety@mail.ru"
    url = "string"
    phone = "89257722254"
    birthdate = "1999-08-13"
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone,
                                       birthdate, isActive=1)
    emp_id = new_employee["id"]
    # Получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1

    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    assert body[-1]["firstName"] == "Петр"
    assert body[-1]["lastName"] == "Петров"
    assert body[-1]["middleName"] == "Петрович"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89257722254"
    assert body[-1]["birthdate"] == "1999-08-13"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id


def test_patch_employee():
    # Создать новую компанию
    name = "Горный хребет"
    descr = "массажная студия"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # Добавить нового сотрудника
    firstName = "Семен"
    lastName = "Семенов"
    middleName = "Семеныч"
    email = "semen@mail.ru"
    url = "string"
    phone = "89992224411"
    birthdate = "2001-08-13"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone, birthdate,
                                       isActive)
    emp_id = new_employee["id"]

    # Получить список сотрудников новой компании
    api.get_employees_list(companyId)

    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Васильев"
    new_email = "vas@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url,
                               new_phone, new_isActive)
    assert edited["email"] == "vas@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False
# Список объектов

from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Iphone", "15 pro max", "+7 900 000 00 01")
phone2 = Smartphone("Iphone", "14 pro max", "+7 900 000 00 02")
phone3 = Smartphone("Iphone", "13", "+7 900 000 00 03")
phone4 = Smartphone("Iphone", "12 pro", "+7 900 000 00 04")
phone5 = Smartphone("Iphone", "11", "+7 900 000 00 05")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} , {phone.phone_number}")
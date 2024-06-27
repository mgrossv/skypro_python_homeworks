# Вложенные классы

from address import Address
from mailing import Mailing
to_address = Address("12345", "Москва", "проспект Ленина", "1" ,"2")
from_address = Address("56789", "Санкт-Петербург", "Невский проспект", "3", "4")
mailing = Mailing(to_address, from_address, 789,"RA0123456" )

print(f"Отправление {mailing.track} из {mailing.from_address.index},{mailing.from_address.city},"
      f"{mailing.from_address.street},{mailing.from_address.house}-{mailing.from_address.apart}"
      f" в {mailing.to_address.index},{mailing.to_address.city},{mailing.to_address.street},"
      f"{mailing.to_address.house}-{mailing.to_address.apart}. Стоимость {mailing.cost} рублей.")

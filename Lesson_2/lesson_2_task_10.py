# Банковское приложение

# Дано: пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых.
# Каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада.
# На добавленное в следующем году тоже будут проценты.

x = int(input("Сумма вклада:"))
y = int(input("На сколько лет:"))

def bank():
    procent = 0.10
    sum = x * (1 + procent) * y 
    print("Итоговая сумма вклада + годовые проценты :", (sum))
bank()
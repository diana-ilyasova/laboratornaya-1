salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
a = 0
month = 1
while month <= months:
    month = month + 1
    a = spend - salary
    spend = (spend * increase) + spend
    money_capital = money_capital + a



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))


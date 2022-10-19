money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= 0:
    money_capital -= (spend - salary)
    spend *= increase
    if money_capital >= 0:
        month += 1

print(month)

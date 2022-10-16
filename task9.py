salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
i = 1

while i <= months:
    need_money += spend
    need_money -= salary
    spend *= increase
    i += 1

print(round(need_money))

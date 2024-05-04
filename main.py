# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal
from bankomat.func import deposit, withdraw, exit, operations, current_balance
from bankomat.messages import enter, start_menu, replenishment_menu, error_pin, cur_balance

pin = 1111

pin_count = 3
while pin_count > 0:
    inp_pin = int(input(enter + f'Кол-во попыток {pin_count}:'))
    if inp_pin == pin:
        main_menu = True
        while main_menu:
            choice = int(input(start_menu))
            match choice:
                case 1:
                    amount = decimal.Decimal(input(replenishment_menu))
                    deposit(amount)
                    print(operations[-1])
                case 2:
                    amount = decimal.Decimal(input(replenishment_menu))
                    withdraw(amount)
                    print('Последняя операция:')
                    print(operations[-1])
                case 3:
                    print(cur_balance(current_balance[-1]))
                case 4:
                    exit()
                    print(operations[-1])
                    main_menu = False
        pin_count = 0
    pin_count -= 1
else:
    print(error_pin)

import bankomat.func
from bankomat.func import MULTIPLICITY, RICHNESS_PERCENT

enter = 'Введите пин код, '
error_pin = 'До свидания!'
start_menu = (f'*****************************************************************\n'
              f'ВНИМАНИЕ ПОСЛЕ КАЖДОЙ 3 ОПЕРАЦИИ НАЧИСЛЯЕТСЯ ДЕПОЗИТ В РАЗМЕРЕ 3%\n1. Пополнение \n2. Снятие \n'
              f'3. Текущий баланс\n4. Выйти\n Выберите пункт меню:')
replenishment_menu = 'Введите сумму пополнения: '
multiplicity_check = f'Сумма должна быть кратной {MULTIPLICITY} у.е.'


def cur_balance(cur_bal):
    return (f'==============================\n'
            f'Текущий баланс {cur_bal} у.е.\n'
            f'==============================')

def refill(amount, bank_account):
    return f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.'


def withdrawal(amount, percent, bank_account):
    return f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е.'


def insufficient_funds(amount, percent, bank_account):
    return f'Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е.'


def nalog(percent, bank_account):
    return f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.'


def not_nalog(bank_account):
    return f'Возьмите карту на которой {bank_account} у.е.'


def proc_depozit(proc):
    return (f'======================================\n'
            f'Начислен депозит в размере {proc} у.е.\n'
            f'======================================')

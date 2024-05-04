import decimal


MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(5_000_000)

bank_account = decimal.Decimal(0)
current_balance = [0]
count = 0
operations = [0]


def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        # print(multiplicity_check)
        return False
    return True


def deposit(amount):
    """Пополнение счета"""
    from bankomat.messages import multiplicity_check, refill, proc_depozit
    global bank_account, count, current_balance
    if not check_multiplicity(amount):
        print(multiplicity_check)
        exit()
        return False
    count += 1
    if count >= 3:
        bank_account += bank_account * PERCENT_DEPOSIT
        print(proc_depozit(bank_account * PERCENT_DEPOSIT))
        count = 0
    bank_account += amount
    current_balance.append(bank_account)
    operations.append(refill(amount, bank_account))
    return True


def withdraw(amount):
    """Снятие денег"""
    from bankomat.messages import withdrawal, insufficient_funds, multiplicity_check
    global bank_account, count, current_balance
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if not check_multiplicity(amount):
        print(multiplicity_check)
        return False
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        current_balance.append(bank_account)
        operations.append(withdrawal(amount, percent, bank_account))
    else:
        operations.append(insufficient_funds(amount, percent, bank_account))


def exit():
    from bankomat.messages import nalog, not_nalog
    global bank_account, operations, current_balance
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        current_balance.append(bank_account)
        operations.append(nalog(percent, bank_account))
    else:
        operations.append(not_nalog(bank_account))

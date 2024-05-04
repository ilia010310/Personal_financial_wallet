import time

from main import Wallet

# создаем кошелек и файл с названием wallet.json
my_wallet = Wallet('wallet.json')

# добавляем первый доход:
my_wallet.income(30000, 'Зарплата')
print('Добавили 30 000')

# проверяем баланс:
print('Баланс:', my_wallet.get_balance())

time.sleep(2)

# добавляем первый расход:
my_wallet.expense(8000, 'Одежда')
print('Потратили 8 000')

time.sleep(2)

# проверяем баланс:
print('Баланс:', my_wallet.get_balance())

time.sleep(2)

# добавляем расходы:
for i in range(10000, 15000, 1000):
    my_wallet.expense(i, 'Продукты')
print('Потратили 10 000 + 11 000 + 12 000 + 13 000 + 14 000 = 60 000')

# проверяем баланс:
print('Баланс:', my_wallet.get_balance())

time.sleep(2)

# добавляем доходы:
for i in range(5000, 9000, 1000):
    my_wallet.income(i, 'Дивиденды')
print('Заработали: 5 000 + 6 000 + 7 000 + 8 000 = 26 000')

time.sleep(2)

# проверяем баланс:
print('Баланс:', my_wallet.get_balance())

time.sleep(2)

# проверяем отдельно все расходы:
print('Все расходы:', my_wallet.get_expenses())

time.sleep(2)

# проверяем отдельно все доходы:
print('Все доходы:', my_wallet.get_incomes())

time.sleep(2)

print('Изменяем доход с 30 000 до 60 000')
# изменяем операцию дохода с id=1:
my_wallet.edit_operation(
    1, "2024-05-04",
    "Доход", 60000,
    'Зарплата'
)

print('Баланс:', my_wallet.get_balance())

time.sleep(2)

print("Выводим все данные по категории 'Расход'")
print(my_wallet.search_category('Расход'))

time.sleep(2)

print("Выводим все данные по сумме 60 000")
print()
print(my_wallet.search_summ(60000))

print("Выводим все данные по дате '2024-05-04'")
print()
print(my_wallet.search_date('2024-05-04'))


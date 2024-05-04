import json
import datetime
import os
import time


class Wallet:


    def __new__(cls, wallets_name: str):
        # Если еще нет такого файла - создаем его с пустым списком
        if not os.path.exists(wallets_name):
            with open(wallets_name, 'w', encoding='utf-8') as file:
                json.dump([], file)
        return super().__new__(cls)

    def __init__(self, wallets_name: str):
        # привязываем название кошелька к нашей сущности
        self.data = wallets_name
        self.balance = 0
        # Если файл уже существует, то нам нужно посчитать значения баланса и последнего id
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            if operations == []:
                self.counter = 0
            else:
                for operation in operations:
                    if operation['category'] == 'Расход':
                        self.balance -= operation['summ']
                    elif operation['category'] == 'Доход':
                        self.balance += operation['summ']
                self.counter = operations[-1]['id']

    def income(self, num: int | float, description: str) -> None:
        """Adding income with description"""
        self.counter += 1
        income = {
            'id': self.counter,
            'date': str(datetime.date.today()),
            'category': 'Доход',
            'summ': num,
            'description': description
        }
        with open(self.data, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(income)
            with open(self.data, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

        self.balance += num

    def expense(self, num: int | float, description: str) -> None:
        """Adding an expense with a description"""
        self.counter += 1
        expense = {
            'id': self.counter,
            'date': str(datetime.date.today()),
            'category': 'Расход',
            'summ': num,
            'description': description
        }

        with open(self.data, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(expense)
            with open(self.data, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

        self.balance -= num

    def get_expenses(self) -> int | float:
        """Get information about all expenses"""
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            total_expenses = 0
            for operation in operations:
                if operation['category'] == 'Расход':
                    total_expenses += operation['summ']
        return total_expenses

    def get_incomes(self) -> int | float:
        """Get information about all incomes"""
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            total_incomes = 0
            for operation in operations:
                if operation['category'] == 'Доход':
                    total_incomes += operation['summ']
        return total_incomes

    def get_balance(self):
        """Get information about the current balance"""
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            self.balance = 0
            if operations != []:
                for operation in operations:
                    if operation['category'] == 'Расход':
                        self.balance -= operation['summ']
                    elif operation['category'] == 'Доход':
                        self.balance += operation['summ']
                return self.balance
            else:
                return 0

    def edit_operation(self, id: int, date: str,
                       category: str, summ: int | float, description: str) -> None:
        """Editing a specific entry with specific data"""
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            for operation in operations:
                if operation['id'] == id:
                    operation['date'] = date
                    operation['category'] = category
                    operation['summ'] = summ
                    operation['description'] = description
            with open(self.data, 'w', encoding='utf-8') as f:
                json.dump(operations, f, indent=2)


    def search_category(self, category: str) -> str:
        answer = ''
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            for operation in operations:
                if operation['category'] == category:
                    answer += (
                        f'id: {operation["id"]},\n'
                        f'date: {operation["date"]},\n'
                        f'category: {operation["category"]},\n'
                        f'summ: {operation["summ"]},\n'
                        f'description: {operation["description"]}\n\n'
                    )
        return answer

    def search_date(self, date: str) -> str:
        answer = ''
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            for operation in operations:
                if operation['date'] == date:
                    answer += (
                        f'id: {operation["id"]},\n'
                        f'date: {operation["date"]},\n'
                        f'category: {operation["category"]},\n'
                        f'summ: {operation["summ"]},\n'
                        f'description: {operation["description"]}\n'
                    )
        return answer

    def search_summ(self, summ: int | float) -> str:
        answer = ''
        with open(self.data, 'r', encoding='utf-8') as file:
            operations = list(json.load(file))
            for operation in operations:
                if operation['summ'] == summ:
                    answer += (
                        f'id: {operation["id"]},\n'
                        f'date: {operation["date"]},\n'
                        f'category: {operation["category"]},\n'
                        f'summ: {operation["summ"]},\n'
                        f'description: {operation["description"]}\n'
                    )
        return answer

    def __str__(self):
        return f'Название кошелька: {self}, баланс = {self.balance}'




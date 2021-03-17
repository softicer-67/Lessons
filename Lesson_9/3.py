from colorama import Fore as F, Style as S


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Иван', 'Иванов', 'Директор', 150000, 15000)
b = Position('Петр', 'Петров', 'Зам.Начальника', 60000, 5000)

print(f'Работник: {F.GREEN}{a.get_full_name()}{S.RESET_ALL}| Должность: {F.GREEN}{a.position}{S.RESET_ALL}| Доход с учетом премии: {F.CYAN}{a.get_total_income()}{S.RESET_ALL} руб.')
print(f'Работник: {F.GREEN}{b.get_full_name()}{S.RESET_ALL}| Должность: {F.GREEN}{b.position}{S.RESET_ALL}| Доход с учетом премии: {F.CYAN}{b.get_total_income()}{S.RESET_ALL} руб.')

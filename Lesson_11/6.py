class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input('Введите наименование: ').lower()
            unit_p = int(input('Введите цену за ед: '))
            unit_q = int(input('Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список:\n {self.my_store}')
        except:
            return 'Ошибка ввода данных'

        print('Для выхода: Q, продолжение: Enter')
        q = input('')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад:\n {self.my_store_full}')
            return 'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'картридж на {self.numb} копий'


class Scanner(Store):
    def to_scan(self):
        return f'картридж на {self.numb} копий'


class Copier(Store):
    def to_copier(self):
        return f'картридж на {self.numb} копий'


unit_1 = Printer('Epson', 2000, 5, 20000)
unit_2 = Scanner('Canon', 1200, 5, 25000)
unit_3 = Copier('Xerox', 1500, 1, 30000)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

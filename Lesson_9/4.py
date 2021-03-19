class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Старт'

    def stop(self):
        return f'{self.name} Стоп'

    def turn_left(self):
        return f'{self.name} Влево'

    def turn_right(self):
        return f'{self.name} Вправо'

    def show_speed(self):
        return f'Скорость {self.name} = {self.speed} км/час'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} {self.speed} выше допустимой!'
        else:
            return f'Скорость {self.name} = {self.speed} км/час'


class SportCar(Car):
    def show_speed(self):
        return f'Скорость {self.name} = {self.speed} км/час'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} {self.speed} выше допустимой!'
        else:
            return f'Скорость {self.name} = {self.speed} км/час'


class PoliceCar(Car):
    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed} км/час'

    def police(self):
        if self.is_police:
            return f'{self.name} - Полицейская машина'
        else:
            return f'{self.name} - Не полицейская машина'


a = TownCar(50, 'Красный', 'Volvo', True)
b = WorkCar(70, 'Зеленый', 'Opel', False)
c = SportCar(120, 'Черный', 'Mersedes', False)
d = Car(80, 'Бежевый', 'Жигули', False)
e = PoliceCar(60, 'Белый', 'Audi',  True)

print(f'{a.show_speed()} | {a.go()} | {a.stop()} | {a.color} | {a.is_police}')
print(f'{b.show_speed()} | {b.turn_left()} | {b.name} | {b.color} | {b.is_police}')
print(f'{c.show_speed()} | {c.turn_right()} | {c.name} | {c.color} | {c.is_police}')
print(f'{d.show_speed()} | {d.go()} | {d.stop()} | {d.color} | {d.is_police}')
print(f'{e.name} полицейская машина ? {e.is_police}')

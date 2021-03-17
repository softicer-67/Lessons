class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'{self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'{self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'{self.title}. Запуск отрисовки маркером'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

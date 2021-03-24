class Error:
    def __init__(self, *num):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_list.append(val)
                print(f'Список: {self.my_list}\n')
            except:
                print('Недопустимое значение - строка и булево')
                go = str(input('Y - попробовать еще раз; N - Выход):'))
                if go == 'Y' or go == 'y':
                    print(try_ex.my_input())
                elif go == 'N' or go == 'n':
                    return 'Выход'


try_ex = Error(1)
print(try_ex.my_input())

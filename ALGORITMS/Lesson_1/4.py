"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random


def menu():
    print('\n\tМЕНЮ:\n\n\
    [1] Вывести случайное целое число\n\
    [2] Случайное вещественное число\n\
    [3] Случайный символ\n\
    [0] Выход')


def num_choice():
    print('Введите интервал: ')
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    if a > b:
        return random.randint(b, a)
    return random.randint(a, b)


def alpha_choice():
    print('Введите интервал: ')
    c = input('Первая буква: ')
    d = input('Вторая буква: ')
    list_abc = [chr(i) for i in range(ord(c), ord(d) + 1)]
    if ord(c) > ord(d):
        list_abc = [chr(i) for i in range(ord(d), ord(c) + 1)]
    return random.choice(list_abc)


menu()
option = input()

while option != '0':
    if option == '1':
        print(num_choice())
    elif option == '2':
        print(float(num_choice()))
    elif option == '3':
        print(alpha_choice())
    else:
        print('Только [1], [2], [3] или [0]')

    if __name__ == '__main__':
        option = input()







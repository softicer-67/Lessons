def menu():
    print('[+] Сложение\n'
          '[-] Вычитание\n'
          '[*] Умножение\n'
          '[/] Деление\n'
          '[0] Выход')


menu()
option = input()

while option != '0':
    if option == '+':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} + {b} =', a + b)
    elif option == '-':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} - {b} =', a - b)
    elif option == '*':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} * {b} =', a * b)
    elif option == '/':
        try:
            a = int(input('Введите первое число:'))
            b = int(input('Введите второе число:'))
            print(f'{a} / {b} =', round(a / b, 4))
        except ZeroDivisionError:
            print('Ошибка! На <0> делить нельзя!')
    else:
        print('Ошибка, введите правильный  символ:')
    menu()
    option = input()


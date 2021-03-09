print('\nСкрипт для чтения данных\n')

with open('bakery.csv', 'r', encoding='utf-8') as f:
    for i in f:
        i = str(i)
        print(f'{i}', end='')

print('\nСкрипт чтения данных с заданного числа до конца\n')
num_start = input('Введите число: ')
with open('bakery.csv', 'r') as f:
    num = f.readlines()
    for i in range(int(num_start) - 1, len(num)):
        print(num[i], end='')

print('\nСкрипт чтения данных с заданного числа по второе заданное число: \n')
num_start = input('Введите первое число: ')
num_end = input('Введите второе число: ')
with open('bakery.csv', 'r') as f:
    num = f.readlines()
    for i in range(int(num_start) - 1, int(num_end)):
        print(num[i], end='')



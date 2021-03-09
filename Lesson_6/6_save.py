print('\nСкрипт для записи данных\n')

while True:

    save = input(f'Записать данные в файл: ')
    if save.isalpha():
        print('Это не число! Попробуйте еще: ')
    else:
        lines = 1
        with open('bakery.csv', 'r+', encoding='utf-8') as f:
            for line in f:
                lines += 1
            f.write(f'{lines}: {save}\n')

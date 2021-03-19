print('\nСкрипт для записи данных\n')

while True:

    save = input(f'Записать данные в файл: ')
    if save.isalpha():
        print('Это не число! Попробуйте еще: ')
    else:
        lines = 1
        with open('shop.txt', mode='r+', encoding='utf-8') as file:
            for line in file:
                lines += 1
            file.write(f'{lines}: {save}\n')

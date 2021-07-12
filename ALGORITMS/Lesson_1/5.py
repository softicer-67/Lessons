# """
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# """

a, b = [i.upper() for i in input('Введите 2 буквы латинского алфавита слитно: ')]

# генерим алфавит
alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Определяем какая буква по счету
letter1 = alpha.index(a) + 1
letter2 = alpha.index(b) + 1

# подсчитываем колличество между бувами
interval = letter2 - letter1 - 1

# исправим на правильное написание слов
text = []
if interval % 10 in [1]:
    text = 'буква'
elif interval % 10 in [2, 3, 4]:
    text = 'буквы'
else:
    text = 'букв'

print('Первая буква стоит на', letter1, 'месте')
print('Вторая буква стоит на', letter2, 'месте')
print('Между ними', interval, text)

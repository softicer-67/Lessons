'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

number = input('Введите число: ')
numeral = input('Введите цифру, которую необходимо посчитать: ')

result = 0
for i in number:
    if i == numeral:
        result += 1
print(f'В числе {number} цифр {numeral} = {result} шт.')


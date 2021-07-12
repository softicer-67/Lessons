"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# a, b = input('Введите 2 буквы латинского алфавита: ')
#
# x = len(alphabet)

number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")
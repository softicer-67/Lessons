# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('\n1 Вариант. Введите трехзначное целое число: '))

a = number // 100
b = number % 100 // 10
c = number % 10

print('\nСумма цифр: ', a + b + c)
print('Произведение цифр: ', a * b * c)


num = input('\n2 Вариант. Введите трехзначное целое число: ')
summa = 0
umn = 1
for i in num:
    summa += int(i)
    umn *= int(i)

print('\nСумма цифр: ', summa)
print('Произведение цифр: ', umn)




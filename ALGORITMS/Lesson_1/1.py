#  1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трехзначное число: '))

d1 = x // 100
d2 = x % 100 // 10
d3 = x % 10

print('Сумма цифр трехзначного числа: ', d1 + d2 + d3)
print('Произведение цифр трехзначного числа: ', d1 * d2 * d3)
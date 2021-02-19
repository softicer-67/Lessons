print('\n\tCписок, состоящий из кубов нечётных чисел от 1 до 1000\n')

x = range(1000)
res = []
for i in x:
    if i % 2 != 0:
        res.append(i ** 3)
print(list(res))


print('\n\tВычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7\n')

summa_1 = []
for i in res:
    num = list(str(i))
    num1 = [int(c) for c in num]
    summa = sum(num1)
    if summa % 7 == 0:
        summa_1.append(i)
        print(summa, end=', ')

print('\n\tCумма тех чисел из этого списка, сумма цифр которых делится нацело на 7 = ', sum(summa_1))


print('\n\tК каждому элементу списка добавляем 17 и заново вычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7')



summa_1 = []
for i in res:
    num = list(str(i + 17))
    num1 = [int(c) for c in num]
    summa = sum(num1)
    if summa % 7 == 0:
        summa_1.append(i)
        print(summa, end=', ')

print('\n\tCумма тех чисел из этого списка, сумма цифр которых делится нацело на 7 = ', sum(summa_1))

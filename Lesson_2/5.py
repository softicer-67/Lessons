price_product = [57.8, 46.51, 97, 28.12, 88.14, 22.15, 170.99, 250, 99, 1450, 580.99]
print()


def sort(product):
    for i in price:
        x = str("%.2f" % i)
        x1 = x.replace('.', ' руб ')
        print(x1 + ' коп', end=', ')


print('\nСортировка по возрастанию:\n')
price = sorted(price_product)
sort(price)

print('\n\nСписок не изменился\t', price_product)
print('\nСортировка по убыванию:\n')

price.reverse()
sort(price)

print('\n\nЦена пяти самых дорогих товаров. Вывод цены этих товаров по возрастанию\n')
print(price[4::-1])

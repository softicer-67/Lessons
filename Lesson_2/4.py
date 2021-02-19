arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
text = []
names = []

for i in arr:
    arr = i.split()
    names = arr.pop().title()
    arr.extend(names.split())
    print(' '.join(arr))
    print(f'Привет, {names}!')

print('\nВариант без  новых списков:\n')

name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in name:
    name = i.split()
    name1 = name[-1].title()
    print(' '.join(name[:-1]), name1)
    print(f'Привет, {name1}!')

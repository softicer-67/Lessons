duration = (int(input('Введите колличество секунд: ')))

d = duration // 60 // 60 // 24  	# День   = 86400 секунд
h = duration // 60 // 60 % 24   	# Час    = 3600 секунд
m = duration // 60 % 60         	# Минута = 60 секунд
s = duration % 60              	    # Секунда

if duration < 60:
    print(f'{s} сек')
if duration >= 60 and duration < 3600:
    print(f'{m} мин {s} сек')
if duration >= 3600 and duration < 86400:
    print(f'{h} час {m} мин {s} сек')
if duration >= 86400:
    print(f'{d} дн {h} час {m} мин {s} сек')

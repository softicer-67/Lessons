arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(arr)):
    summa = 0
    lasts = ''
    num = ''

    for j in arr[i]:
        if j in nums:
            summa += 1
            num += j
        else:
            lasts += j

    if summa > 0 and summa < 2 and len(arr[i]) >= summa:
        arr[i] = lasts + '0' + num

print(' '.join(arr))


with open('nginx_logs.txt', 'r') as f:
    full = []
    for i in f:
        x = i.split(' ')
        full.append(x[0])

    uni_ip = []
    for j in full:
        if j not in uni_ip:
            uni_ip.append(j)

    repeat = {}
    for i in uni_ip:
        repeat[i] = 0

    for i in full:
        repeat[i] += 1

    repeat = list(repeat.items())
    repeat.sort(reverse=True, key=lambda ip: ip[1])
    print(f'с IP: {repeat[0][0]}, отправлено запросов: {repeat[0][1]} <---- Самый могучий Спамер ;-)')
    print(f'с IP: {repeat[1][0]}, отправлено запросов: {repeat[1][1]}')
    print(f'с IP: {repeat[2][0]}, отправлено запросов: {repeat[2][1]}')

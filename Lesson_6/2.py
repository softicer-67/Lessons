
with open('nginx_logs.txt', 'r') as f:
    full = []
    for line in f:
        x = line.split(' ')
        full.append(x[0])

    uni_ip = []
    for i in full:
        if i not in uni_ip:
            uni_ip.append(i)

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

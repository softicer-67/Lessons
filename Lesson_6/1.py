
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        x = line.split(' ')
        print((x[0], x[5], x[6]))







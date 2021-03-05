
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        x = line.replace('"', '')
        x = x.split(' ')
        x = x[0], x[5], x[6]
        print(x)








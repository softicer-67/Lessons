import os

sizes = []
res = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
for i in os.scandir('some_data'):
    if i.name.endswith('.bin'):
        s = os.stat(i)
        size = s.st_size
        sizes.append(size)

for i in sizes:
    if i < 100:
        res[100] += 1
    elif i < 1000:
        res[1000] += 1
    elif i < 10000:
        res[10000] += 1
    elif i < 100000:
        res[100000] += 1

print(res)

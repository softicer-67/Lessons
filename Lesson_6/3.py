from sys import exit


with open('users.csv', mode='r', encoding='utf-8-sig') as i:
    user = [i.rstrip('\n') for i in i]

with open('hobby.csv', 'r', encoding='utf-8-sig') as i:
    hobby = [i.rstrip('\n') for i in i]


res = {}

if len(hobby) > len(user):
    exit(1)

else:

    for i in range(len(user)):
        try:
            res[user[i]] = hobby[i]
        except IndexError:
            res[user[i]] = None

print(res)

with open('dictionary.txt', 'w', encoding='utf-8') as f:
    f.write(str(res))

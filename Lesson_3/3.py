
def thesaurus(*args):
    res = {}
    for i in args:
        if i[0] in res:
            res[i[0]].append(i)
        else:
            res[i[0]] = [i]
    return res


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


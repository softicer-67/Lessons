class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def reload(self):
        res = ''
        for i in self.lists:
            res += str(i) + '\n'
            res = res.replace(',', '')
            res = res.replace('[', '')
            res = res.replace(']', '')
        return res


a = [[31, 22], [37, 43], [51, 86]]
b = [[2, 5, 32], [2, 4, 6], [-1, 64, -8]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]

m1 = Matrix(a)
m2 = Matrix(b)
m3 = Matrix(c)

print(f"{m1.reload()}\n{m2.reload()}\n{m3.reload()}")


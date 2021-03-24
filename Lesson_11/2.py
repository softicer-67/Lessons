class DivisionByNull:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def divide_by_null(num_1, num_2):
        try:
            return num_1 / num_2
        except:
            return f"Деление на ноль недопустимо"


div = DivisionByNull(20, 80)
print(div.divide_by_null(50, 0))
print(div.divide_by_null(30, 0.1))
print(div.divide_by_null(10, 0))

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = [i for i in day_month_year.split() if i != '-']
        # for i in day_month_year.split():
        #     if i != '-':
        #         my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Все верно: {day, month, year}'
                else:
                    return f'Ошибка год: {day, month, year}'
            else:
                return f'Ошибка месяц: {day, month, year}'
        else:
            return f'Ошибка день: {day, month, year}'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'


d = Data('21 - 03 - 2021')
print(d)
print(Data.valid(5, 8, 2023))
print(d.valid(7, 13, 2021))
print(Data.valid(4, 2, 2021))

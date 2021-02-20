import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nums):
    res = []
    """функция возвращает n шуток, сформированных из случайных слов,
    взятых из трёх списков"""
    for i in range(nums):
        a = random.choice(nouns)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        res.append(f'{a.title()} {b} {c}')
    print(res)


get_jokes(3)

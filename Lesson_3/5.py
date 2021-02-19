import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nums):
    for i in range(nums):
        a = random.choice(nouns)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        print(a.capitalize(), b, c)


get_jokes(2)

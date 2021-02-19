number = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(num):
    if num[0].isupper():
        num = num.lower()
        print(number[num].title())
    elif num in number:
        print(number[num])
    else:
        print('None')


num_translate_adv("One")
num_translate_adv("two")
num_translate_adv("Three")
num_translate_adv("four")
num_translate_adv("Five")
num_translate_adv("six")
num_translate_adv("Seven")
num_translate_adv("eight")
num_translate_adv("Nine")
num_translate_adv("ten")
num_translate_adv("twenty one")

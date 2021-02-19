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


def num_translate(num):
    if num in number:
        print(number[num])
    else:
        print('None')


num_translate("one")
num_translate("two")
num_translate("three")
num_translate("four")
num_translate("five")
num_translate("six")
num_translate("seven")
num_translate("eight")
num_translate("nine")
num_translate("ten")
num_translate("twenty one")
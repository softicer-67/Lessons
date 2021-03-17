def type_logger(func):
    def wrapper(*args):
        result = f'{args[-1]}: {type(*args)}'
        result1 = f'{func.__name__} ({args[-1]}: {type(*args)})'

        return result + '\n' + result1
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)


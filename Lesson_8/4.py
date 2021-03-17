def val_checker(x):
    def _val_checker(func):
        def wrapper(args):
            result = func(args)
            if result > 0:
                return result
            else:
                return ''.join(f'ValueError: wrong val {args}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
b = calc_cube(-5)
print(b)

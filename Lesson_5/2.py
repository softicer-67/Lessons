def num_generator(n):
    num = (num for num in range(1, n + 1, 2))
    return num


nums_gen = num_generator(15)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))

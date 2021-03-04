tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Геннадий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

new_gen = [el + i for el in tutors for i in klasses]
print(new_gen)


# new_gen = ((tutors[i], klasses[i]) for j in range(len(klasses)) for i in range(len(tutors)))
# if klasses < tutors:
#     klasses.append(None)
#
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(next(new_gen))
# print(type(new_gen))

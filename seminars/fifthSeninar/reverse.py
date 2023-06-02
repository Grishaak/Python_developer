# import random
#
# number = int(input("Введите число: "))
# n_list = [random.randrange(1, 10) for i in range(number)]
# print(n_list)
# n_list = n_list[::-1]
# print(n_list)


def sequence(size):
    if size == 0:
        return ""
    number = input("введите число: ")
    return sequence(size - 1) + number


print(sequence(5))

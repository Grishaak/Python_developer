import random

values = [random.randint(1, 10) for i in range(10)]
print(values)


# def transformation(val, mult):
#     some_list = [i * mult for i in val]
#     return some_list


# multi = 1
trans_values = list(map(lambda i: i * 1, values))
print(trans_values)
trans_values[0] = 10
print(trans_values)
print(values)
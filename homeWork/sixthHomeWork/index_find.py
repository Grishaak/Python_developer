import random

size_lsit = int(input("Введите размер списка: "))
min_range = int(input("Введите минимальный диапазон: "))
max_range = int(input("Введите максимальный диапазон: "))
#
# new_list = []
# index_list = []
# for i in range(size_lsit):
#     new_list.append(random.randint(-10, 30))
#     if min_range < new_list[i] < max_range:
#         index_list.append(i)
# print(
#     f"Элементы списка - {new_list}\nи индексы элементов вошедшие в диапазон от \n({min_range} до {max_range}) - {index_list}")

new_list = [random.randint(-10, 10) for i in range(size_lsit)]
some_list = list(filter(lambda i: min_range < new_list[i] < max_range, range(len(new_list))))
print(
    f"Элементы списка - {new_list}\nи индексы элементов вошедшие в диапазон от \n({min_range} до {max_range}) - {some_list}")

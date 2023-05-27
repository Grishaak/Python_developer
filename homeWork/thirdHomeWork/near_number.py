# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя
# строка содержит число X

import random

size_n = int(input("Размер списка: "))
my_list = []
near_number = int()
for i in range(size_n):
    my_list.append(random.randint(-100, 100))
new_list = my_list
number_x = int(input("\nВведите искомое число: "))
if number_x in my_list:
    print("Такой элемент уже есть")
else:
    my_list.append(number_x)
    print(my_list)
    my_list = sorted(my_list, reverse=False)
    print(my_list)
    index_num_x = my_list.index(number_x)
    if index_num_x == len(my_list) - 1:
        near_number = my_list[index_num_x - 1]
    elif index_num_x == 0:
        near_number = my_list[index_num_x + 1]
    else:
        near_number = my_list[index_num_x - 1]
        if number_x - near_number >= my_list[index_num_x + 1] - number_x:
            near_number = my_list[index_num_x + 1]
print(near_number)

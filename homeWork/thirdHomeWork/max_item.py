# Задача 16: Требуется вычислить,
# сколько раз встречается некоторое число
# X в массиве A[1..N]. Пользователь в
# первой строке вводит натуральное число
# N – количество элементов в массиве. В
# последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
import random

size_n = int(input("Размер списка: "))
my_list = []
for i in range(size_n):
    my_list.append(random.randint(1, 10))
number_x = int(input("\nВведите искомое число: "))
if number_x in my_list:
    print(f"Число {number_x} встречается - {my_list.count(number_x)} раз ")
else:
    print("Такого числа нет!")
print(my_list)
# print(number_x)

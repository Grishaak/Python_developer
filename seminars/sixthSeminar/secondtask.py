# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
import random

number = int(input("Введите число: "))

my_list = [random.randint(1, 6) for i in range(number)]
count = 0
for item in range(len(my_list) - 1):
    if (item > 0) and (item < len(my_list)):
        if (my_list[item] > my_list[item - 1]) and (my_list[item] > my_list[item + 1]):
            count += 1
print(my_list)
print(count)
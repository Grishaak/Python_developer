# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
import random

my_list = []
for i in range(10):
    my_list.append(random.randint(1, 10))
print(my_list)
count = 0
for i in range(len(my_list) - 1):
    if my_list[i] < my_list[i + 1]:
        count += 1
print(count)

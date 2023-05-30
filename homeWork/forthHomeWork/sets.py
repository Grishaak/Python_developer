# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

number_list_one = [random.randint(-10, 10) for i in range(0, 7)]
number_list_two = [random.randint(-10, 10) for j in range(0, 7)]
print(number_list_one)
print(number_list_two)
list = list(set(number_list_one).intersection(number_list_two))
print(sorted(list))
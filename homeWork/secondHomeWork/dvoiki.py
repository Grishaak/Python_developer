# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

number_n = int(input("Введите число N: "))
k = 0
number_two = 2
list_pow = []
while number_two ** k < number_n:
    list_pow.append(number_two ** k)
    k += 1
print(list_pow)
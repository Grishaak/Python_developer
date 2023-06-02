# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
import random

number = int(input("Введите число: "))
my_list = []
for i in range(number):
    my_list.append(random.randint(1, 5))

def journal(num):
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i] == max(my_list):
            my_list[i] = min(my_list)
    return my_list


x = journal(number)
print(x)

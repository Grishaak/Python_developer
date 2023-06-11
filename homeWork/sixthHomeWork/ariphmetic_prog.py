# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

size_prog = int(input("Введите размер: "))
difference = int(input("\nВведите разность: "))
first_num = int(input("\nВведите начало прогрессии: "))

def some(size):
    new_list = [i for i in range(size)]
    return new_list


res = some(size_prog)
res = list(map(lambda i: first_num + ((i + 1) - 1) * difference, res))
print(res)
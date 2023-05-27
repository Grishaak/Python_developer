# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

def my_list(key):
    my_list = [i for i in range(5)]
    print(my_list)
    # if key > len(my_list):
    #     return 0
    for i in range(key):
        my_list.insert(0, my_list.pop(len(my_list) - 1))
    # my_list = my_list[key:] + my_list[0:key]
    return my_list


token = 12

smth = my_list(token)
print(smth)

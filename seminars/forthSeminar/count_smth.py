# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

text = input("Введите текст: ")
text_2 = ""
if " " in text:
    text = text.split()
    for i in text:
        text_2 += i
    text = text_2
new_list = []
print(text)
for item in text:
    if item not in new_list:
        new_list.append(item)
    else:
        new_list.append(item)
        times = new_list.count(item)
        new_list.append(item + str(f"_{times - 1}"))
print(new_list)
new_text = ""
for item in new_list:
    if item not in new_text:
        new_text += f"{item} "
print(new_text)
import random

# Через словарь
my_list = [random.randint(0, 10) for _ in range(20)]
print(my_list)

counter = {}

for item in my_list:
    counter[item] = counter.get(item, 0) + 1
    print(item if counter.get(item) < 2 else (str(item) + "_") + str(counter.get(item) - 1), end = " ")

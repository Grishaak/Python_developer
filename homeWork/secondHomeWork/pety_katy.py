# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
list_k = []
list_n = []
for k in range(1, number1):
    if number1 % k == 0:
        list_k.append(k)
for n in range(1, number1):
    if number1 % n == 0:
        list_n.append(n)
print(list_k)
print(list_n)
for i in list_k:
    for j in list_n:
        if i * j == number1 and i + j == number2:
            print(f"{i} and {j}")

# Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите число: "))
total = 0
while number > 0:
    total += number % 10
    number = number / 10
print(total)
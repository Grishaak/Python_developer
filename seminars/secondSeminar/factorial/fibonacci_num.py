# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

number = int(input("Введите число: "))

fib_1 = 0
fib_2 = 1
position = 2

while fib_2 < number:
    fib_2, fib_1 = fib_2+fib_1, fib_2
    position += 1

if number == fib_2:
    print(f"{fib_2} - {position}")
else:
    print(-1)
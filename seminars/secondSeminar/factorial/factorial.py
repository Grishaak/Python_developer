number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
    factorial = i * factorial
    i +=1
print(factorial)

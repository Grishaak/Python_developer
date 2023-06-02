def simple(num):
    if num in [1, 2]:
        return True
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True

number = 433494437
x = simple(number)
if x:
    print("Простое")
else:
    print("Не простое")
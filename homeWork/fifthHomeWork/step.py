# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def powe(a, b):
    if b == 0:
        return a
    else:
        a = a * powe(a, b - 1)
    return a


a_n = 99
b_n = 532
x = powe(a_n, b_n)
print(len(str(x)))

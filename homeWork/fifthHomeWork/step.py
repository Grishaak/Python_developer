# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def pow_sum(a, b):
    if b <= 1:
        if b == 0:
            return 1
        return a
    a = a * pow_sum(a, b - 1)
    return a


number = 2
number_pow = 0
x = pow_sum(number, number_pow)
print(x)

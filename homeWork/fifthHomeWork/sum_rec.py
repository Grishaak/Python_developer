n = 1000
x = 100


def summary(num, num_x):
    if num >= num_x:
        if num_x == 0:
            return num
        else:
            b = summary(num + 1, num_x - 1)
    else:
        if num == 0:
            return num_x
        else:
            b = summary(num - 1, num_x + 1)
    return b


print(summary(n, x))

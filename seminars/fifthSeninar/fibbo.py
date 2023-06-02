# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


limit = int(input("ВВедите число: "))


def fibbo(limit):
    if limit in [0, 1]:
        return 1
    else:
        return fibbo(limit - 1) + fibbo(limit - 2)

list = []
for i in range(1, limit+1):
    list.append(fibbo(i))
print(list)
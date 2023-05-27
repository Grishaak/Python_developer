# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random

list_numbers = []
for i in range(10):
    list_numbers.append(random.randint(-10, 100))
print(list_numbers)
print(len(set(list_numbers)))

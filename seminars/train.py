# 5. Вагоны в электричке пронумерованы
#  натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются
# от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону
#  едет электричка). В каждом вагоне
# написан его номер. Витя сел в i-й вагон
# от головы поезда и обнаружил, что его
# вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке.
# Напишите программу, которая будет это
# делать или сообщать, что без дополнительной
# информации это сделать невозможно.

# **Input:**

# 3

# 4

# **Output:**

# 6


head = int(input("Номер вагона c головы: "))
tail = int(input("Номер вагона с  хвоста : "))

if head != tail:
    result = (head + tail) - 1 
    print(result)
else:
    print("Нельзя решить")
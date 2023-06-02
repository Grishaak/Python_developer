number = 6
# if number % 2 == 0: - ТАкой же как и ниже оператор
if not number % 2:
    print("Yes")
# if number % 2: - Обратный оператор тк 6 - четное число
list_contacts = [1, 2, 3]
if list_contacts:
    print(*list_contacts)
elif not list_contacts:
    print("ТУт Elif")
else:
    print("Список пуст")
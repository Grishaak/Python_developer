import random


# my_list = list(map(lambda x: not x % 3, my_list))
# print(my_list)
#
# character(objects):
#     objects = list(map(lambda x: x > 3, objects))
#     if False in objects:
#         return "not Same"
#     return "Same"


def same_by(character, objects):
    objects = list(map(character, objects))
    print(objects)
    if False in objects:
        return False
    return True


my_list = [random.randint(2, 10) for i in range(5)]
print(my_list)

print(same_by(lambda x: x % 2 == 0, my_list))

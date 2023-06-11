import random


# my_list = list(map(lambda x: not x % 3, my_list))
# print(my_list)

def character(objects):
    objects = list(map(lambda x: x % 2, objects))
    print(objects)
    if False in objects:
        return 0
    return 1


def same_by(characterist, objects):
    if characterist(objects):
        return 0


my_list = [random.randint(1, 11) for i in range(5)]
print(my_list)

same_by(character(my_list), my_list)
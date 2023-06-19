import random


# from phrases import main_menu
# from ring import Ring


class Brawler(object):
    """Виртуальный боец"""
    __TURN__ = 2
    brawler_list = []

    def __init__(self, name, health=40):
        self.name = name
        self.health = health
        print(f"\n{self.name} боец появился!\n")

    def talk(self):
        return print(f"Меня зовут {self.name}"
                     f" сейчас у меня {self.health} hp"
                     f" мое количество выносливости {self.__TURN__}.")

    def punch(self, enemy):
        if self.__TURN__ > 0:
            print(f"{self.name} готовиться нанести удар рукой!")
            damage = random.randint(0, 5)
            if damage:
                enemy.health -= damage
                print(f"{self.name} наносит {damage} урона {enemy.name}!\n")
            else:
                print(f"Но {self.name} промахивается!\n")
            self.__TURN__ -= 1
        else:
            print(f"У вас нет выносливости, вы падаете и открываетесь для удара!")
            self.__TURN__ -= 1

    def kick(self, enemy):
        if self.__TURN__ > 1:
            print(f"{self.name} замахивается ногой! ")
            damage = random.randint(0, 10)
            if damage:
                enemy.health -= damage
                print(f"{self.name} наносит {damage} урона {enemy.name}!\n")
            else:
                print(f"Но {self.name} промахивается!\n")
            self.__TURN__ -= 2
        else:
            print(f"У вас нет выносливости, вы падаете и открываетесь для удара!")
            self.__TURN__ -= 1

    def super_blow(self, enemy):
        if self.__TURN__ > 3:
            print(f"{self.name} Хватает врага за поясницу!")
            damage = random.randint(0, 18)
            if damage:
                enemy.health -= damage
                print(f"{self.name} наносит {damage} урона {enemy.name}!\n")
            else:
                print(f"Но {self.name} промахивается!\n")
            self.__TURN__ -= 4
        else:
            print(f"У вас нет выносливости, вы падаете и открываетесь для удара!")
            self.__TURN__ -= 1

    def wait_for_turn(self):
        print(f"{self.name} пасует и восстанавливаете выносливость!\n")
        self.__TURN__ += 1
        return self.__TURN__

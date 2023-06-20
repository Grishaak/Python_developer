import random

from brawlers import Brawler
from phrases import game_over as gm, input_error


class Ring(object):
    """Виртуальный ринг"""

# Тут реализуется поведение бойцов на ринге
# В init можно было засунуть по другому бойцов, там внизу показано как я сделал это
# через создание ринга

    ring = []

    def __init__(self):
        self.fight_1 = Brawler.brawler_list[0]
        self.fight_2 = Brawler.brawler_list[1]


# Поведение нашего бойца на ринге

    def action_player(self, choice):
        # flag = self.check_for_win(self.fight_1, self.fight_2)
        flag = True
        while flag:
            if choice == 1:
                self.fight_1.punch(self.fight_2)
            elif choice == 2:
                self.fight_1.kick(self.fight_2)
            elif choice == 3:
                self.fight_1.super_blow(self.fight_2)
            x = random.randint(1, 10)
            if x > 8:
                x = random.randint(0, 16)
                if x >= 6:
                    self.fight_2.__TURN__ += 1
                    print(f"{self.fight_2.name} наносит контрудар!\n")
                    self.fight_2.punch(self.fight_1)
                elif 1 <= x < 6:
                    self.fight_2.__TURN__ += 2
                    print(f"{self.fight_2.name} наносит контрудар!\n")
                    self.fight_2.kick(self.fight_1)
                else:
                    self.fight_2.__TURN__ += 4
                    print(f"{self.fight_2.name} изворачивается и наносит контр удар!\n")
                    self.fight_2.super_blow(self.fight_1)
            flag = False

# Поведение бота против нас

    def action_enemy(self):
        # flag = self.check_for_win(self.fight_1, self.fight_2)
        flag = True
        while flag:
            point_fight = random.randint(0, 4)
            if self.fight_2.__TURN__ <= 0:
                self.fight_2.wait_for_turn()
            elif self.fight_2.__TURN__ == 1:
                if 2 > point_fight >= 0:
                    self.fight_2.wait_for_turn()
                else:
                    self.fight_2.punch(self.fight_1)
            elif 4 > self.fight_2.__TURN__ >= 2:
                if 2 > point_fight >= 0:
                    self.fight_2.wait_for_turn()
                elif (2 > self.fight_2.__TURN__ > 0) and (4 >= point_fight >= 2):
                    self.fight_2.punch(self.fight_1)
                else:
                    self.fight_2.kick(self.fight_1)
            else:
                if point_fight == 0:
                    self.fight_2.wait_for_turn()
                elif point_fight == 1:
                    self.fight_2.punch(self.fight_1)
                elif 4 > point_fight >= 2:
                    self.fight_2.kick(self.fight_1)
                else:
                    self.fight_2.super_blow(self.fight_1)
            flag = False


# Создание как-раз таки самого ринга

    def making_ring(self):
        for _, brawler in enumerate(Brawler.brawler_list, 1):
            print(f"{_} - {brawler.name}")
        your_choice = int(input(f"Ваш выбор от 1 до {len(Brawler.brawler_list)}: "))
        while not 0 < your_choice <= len(Brawler.brawler_list):
            print(input_error)
            your_choice = int(input(f"Ваш выбор от 1 до {len(Brawler.brawler_list)}: "))
        self.fight_1 = Brawler.brawler_list.pop(your_choice - 1)
        self.fight_2 = Brawler.brawler_list.pop(Brawler.brawler_list.index(random.choice(Brawler.brawler_list)))
        self.ring = [self.fight_1, self.fight_2]
        return self.fight_1, self.fight_2


# Проверка на победу
    def check_for_win(self, player, enemy):
        if (player.health < 1) and enemy.health > player.health:
            self.win(enemy, player)
            return 0
        elif (enemy.health < 1) and player.health > enemy.health:
            self.win(player, enemy)
            return 0
        elif (enemy.health < 1) and (player.health < 1):
            return 0
        return 1

    def win(self, player_1, player_2):
        print(f"Боец {player_1.name} победил! ",
              f"{player_2.name} покидает бой.\n")

    def game_over(self):
        self.ring = []
        return print(gm)

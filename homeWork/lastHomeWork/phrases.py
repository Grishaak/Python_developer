from brawlers import Brawler

main_menu = """Главное меню
    1. Создать бойца
    2. Выбрать бойца
    3. Выход. \n"""

fight_menu = """
    1. Удар рукой
    2. Удар ногой
    3. Супер удар
    4. Ожидание
    5. Состояние бойцов
    6. Выйти из ринга
    """

menu_choice = "Выберите пункт меню: "
input_error = "Некорректный ввод!"
new_brawler = "Новый боец появился!"
brawler_choose = "Какого бойца вы бы хотели выбрать?"
check_brawlers = "У вас недостаточно бойцов чтобы начать бой!"
game_over = "Игра окончена. Бойцы идут на отдых."


def call_main_menu(message: str) -> int:
    print(message)
    while True:
        if message in main_menu:
            choice = input(menu_choice)
            if choice.isdigit() and 0 < int(choice) < 4:
                return int(choice)
            print(input_error)
        else:
            choice = input(menu_choice)
            if choice.isdigit() and 0 < int(choice) < 7:
                return int(choice)
            print(input_error)


def check_brawlers_list():
    while len(Brawler.brawler_list) < 2:
        print("У вас недостаточно бойцов чтобы начать бой!")
        create_brawler()


def create_brawler():
    name = input("Введите имя бойца: ")
    fighter = Brawler(name)
    Brawler.brawler_list.append(fighter)

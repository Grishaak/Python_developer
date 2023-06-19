from phrases import main_menu, fight_menu, call_main_menu, check_brawlers_list, create_brawler
from ring import Ring


def start():
    while True:
        choice = call_main_menu(main_menu)
        match choice:
            case 1:
                create_brawler()
            case 2:
                check_brawlers_list()
                ring = Ring()
                your_fighter, enemy_fighter = ring.making_ring()
                while True:
                    choice = call_main_menu(fight_menu)
                    match choice:
                        case 1:
                            ring.action_player(choice)
                            ring.action_enemy()
                            check = ring.check_for_win(your_fighter, enemy_fighter)
                            if not check:
                                ring.game_over()
                                break
                        case 2:
                            ring.action_player(choice)
                            ring.action_enemy()
                            check = ring.check_for_win(your_fighter, enemy_fighter)
                            if not check:
                                ring.game_over()
                                break
                        case 3:
                            ring.action_player(choice)
                            ring.action_enemy()
                            check = ring.check_for_win(your_fighter, enemy_fighter)
                            if not check:
                                ring.game_over()
                                break
                        case 4:
                            your_fighter.wait_for_turn()
                            ring.action_enemy()
                            check = ring.check_for_win(your_fighter, enemy_fighter)
                            if not check:
                                break
                        case 5:
                            your_fighter.talk()
                            enemy_fighter.talk()
                        case 6:
                            ring.game_over()
                            break
            case 3:
                break

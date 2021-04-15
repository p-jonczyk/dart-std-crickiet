import sys
import collections
import constants as con
from general_use_functions import possible_score_standard, exit_protocol


def player_name(number_of_player):
    # get player name
    name_list = list(score_board.keys())
    return name_list[number_of_player - 1]


def player_score(number_of_player):
    # get player score
    points_list = list(score_board.values())
    return points_list[number_of_player - 1]


def create_players(number_of_players):
    # taking users number of players and creating them
    if number_of_players > 0:
        for i in range(number_of_players):
            new_player = input("Podaj nazwę gracza %d: " % (i + 1))
            score_board.update({new_player: con.start_points_crickiet})
            crickiet_board.update({new_player: tab_crickiet()})
    else:
        print("Nieprawidłowa ilość graczy.")
    return score_board


def tab_crickiet():
    tab = list(range(15, 21)) + [25]
    tab *= 3
    tab = sorted(tab)
    return tab


def end_game_tab():
    tab = ['X'] * 21
    return tab


def player_crickiet_tab(number_of_player):
    player_tab = list(crickiet_board.values())
    return player_tab[number_of_player - 1]


def crickiet_dart(throw_score, temp_tab):
    index = temp_tab.index(throw_score)
    temp_tab[index] = 'X'
    return temp_tab


def crickiet_tab_update(throw_score, temp_tab, div, number_of_player, score_dict_throw, player_amount):
    count = 0
    while count < div:
        if throw_score in temp_tab:
            crickiet_dart(throw_score, temp_tab)
            game_end = end_check(number_of_player, temp_tab)
            if game_end == True:
                player = player_name(number_of_player)
                crickiet_board.update({player: temp_tab})
                game_ends(player_amount)
            count += 1

        else:
            update_score(throw_score, number_of_player, score_dict_throw)
            count += 1


def update_score(throw_score, number_of_player, score_dict_throw):
    global temp_score_dict
    temp_score_dict = score_dict_throw.copy()
    temp_dict = crickiet_board.copy()
    temp_dict.pop(player_name(number_of_player))
    for key in temp_dict:
        check_list = temp_dict.get(key)
        if ((throw_score in check_list) or (throw_score / 2 in check_list) or (throw_score / 3 in check_list)):
            temp_score = temp_score_dict.get(key) + throw_score
            score_dict_throw.update({key: temp_score})


def end_check(number_of_player, temp_tab):
    if collections.Counter(temp_tab) == collections.Counter(end_game_tab()):
        return True
    else:
        return False


def game_ends(player_amount):
    print(f"\nGra zakończona.\n")
    for j in range(player_amount):
        print(f"{player_name(j + 1)} -> {player_score(j + 1)}\n")
        print(f"{player_name(j + 1)} -> {player_crickiet_tab(j + 1)}\n")
    print()
    exit_protocol()


def crickiet_game(number_of_player, player_amount):
    tab = tab_crickiet()
    player = player_name(number_of_player)
    temp_tab = player_crickiet_tab(number_of_player).copy()
    global score_board
    score_dict_throw = score_board.copy()
    throws = 0
    while throws < 3:
        try:
            command = input(f"\n{player} ({player_score(number_of_player)}) - rzut {throws + 1}: ").lower()
            throw_score = int(command)
            reset_tab = temp_tab.copy()
            if ((throw_score in tab) or (throw_score / 2 in tab) or ((throw_score / 3 in tab) and (throw_score != 75))):
                if throw_score in temp_tab:
                    reset_tab = temp_tab.copy()
                    crickiet_tab_update(throw_score, temp_tab, 1, number_of_player, score_dict_throw, player_amount)
                    print(temp_tab)
                    throws += 1

                elif throw_score / 2 in temp_tab:
                    throw_score = int(throw_score / 2)
                    reset_tab = temp_tab.copy()
                    crickiet_tab_update(throw_score, temp_tab, 2, number_of_player, score_dict_throw, player_amount)
                    print(temp_tab)
                    throws += 1

                elif throw_score / 3 in temp_tab:
                    throw_score = int(throw_score / 3)
                    reset_tab = temp_tab.copy()
                    crickiet_tab_update(throw_score, temp_tab, 3, number_of_player, score_dict_throw, player_amount)
                    print(temp_tab)
                    throws += 1

                else:
                    update_score(throw_score, number_of_player, score_dict_throw)
                    throws += 1
            elif throw_score in possible_score_standard():
                throws += 1
            else:
                print(con.wrong_throw)

        except ValueError:
            if command == 'exit':
                exit_protocol()
            elif command == 'hard reset':
                throws = 0
                temp_tab = player_crickiet_tab(number_of_player).copy()
                score_dict_throw = score_board.copy()

            elif command == 'reset':
                if throws == 0:
                    print("Nie masz rundy do zresetowania.")

                else:
                    if score_dict_throw is not None:
                        throws -= 1
                        temp_tab = reset_tab
                        score_dict_throw = temp_score_dict.copy()
                        print(temp_tab)

            else:
                print(con.wrong_throw)

    score_board = score_dict_throw.copy()
    crickiet_board.update({player: temp_tab})


# creating dict and flags
score_board = {}
crickiet_board = {}
temp_score_dict = {}
playing = False
game_end = False

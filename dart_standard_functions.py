import constants as con
from general_use_functions import *


def create_players(number_of_players):
    # taking users number of players and creating them
    if number_of_players > 0:
        for i in range(number_of_players):
            new_player = input("Podaj nazwię gracza %d: " % (i + 1))
            score_board.update({new_player: con.start_points_std})
    else:
        print("Nieprawidłowa ilość graczy.")


def player_name(number_of_player):
    # get player name
    name_list = list(score_board.keys())
    return name_list[number_of_player - 1]


def player_score(number_of_player):
    # get player score
    points_list = list(score_board.values())
    return points_list[number_of_player - 1]


def end_check(player):
    # check if players properly ends game according to rules of dart
    while True:
        temp_command = input("Czy wynik wyzerowany double'm ? Y/N\n").lower()
        if temp_command == "y":
            print(f"\nGratulacje !\nWygrał {player}.")
            exit_protocol()
        elif temp_command == "n":
            return None
        else:
            print("Nieprawidłowa komenda.")
            continue


def player_hint(temp_score):
    # gives ending hints for players - which points score to end game
    score = possible_score_standard()
    score.sort(reverse=True)
    score = [0] + score
    hint = []
    for i in score:
        for j in score:
            for k in score:
                if (k % 2 == 0 and k <= 40 and k != 0) and i + j + k == temp_score:
                    if i != 0:
                        hint.append(hint_parts(i)[0])
                    if j != 0:
                        hint.append(hint_parts(j)[0])
                    return hint + [f'D{int(k / 2)}']
                elif k == 50 and i + j + k == temp_score:
                    if i != 0:
                        hint.append(hint_parts(i)[0])
                    if j != 0:
                        hint.append(hint_parts(j)[0])
                    return hint + ['DB']


def hint_parts(d):
    # get prefix of hint numbers (single, double, triple, single/double bull)
    hint = []
    if d <= 20:
        hint.append(f'S{d}')
    if d <= 40 and d % 2 == 0:
        hint.append(f'D{int(d / 2)}')
    if d <= 60 and d % 3 == 0:
        hint += [f'T{int(d / 3)}']
    if d == 50:
        hint += ['DB']
    if d == 25:
        hint += ['SB']
    return hint


def throw(number_of_player):
    # score counting and program behaviour while rounds/throws
    player = player_name(number_of_player)
    temp_score = player_score(number_of_player)
    throws = 0
    while throws < 3:
        try:
            command = input(f"{player} - rzut {throws + 1}: ").lower()
            throw_score = int(command)
            # if throw score is possible to get
            if int(throw_score) in possible_score_standard():
                if temp_score > 0:
                    throws += 1
                    points_left = temp_score - throw_score
                    temp_score = points_left
                    if temp_score == 0:
                        if end_check(player) is None:
                            throws = 3
                            temp_score = player_score(number_of_player)
                        continue
                    if temp_score < 1:
                        throws = 3
                        temp_score = player_score(number_of_player)
                        print("FURAAA !")
                        continue
                    else:
                        print(f"Punkty: {temp_score}")
                        if player_hint(temp_score) is None:
                            pass
                        else:
                            print(*player_hint(temp_score), sep=", ")
                        continue
            else:
                print(con.wrong_throw)
                continue
        # different user commends or ValueError
        except ValueError:
            # giving user possibility to exit or reset round
            if command == "exit":
                exit_protocol()
            elif command == "hard reset":
                throws = 0
                temp_score = player_score(number_of_player)
                print("Runda zresetowana.")
                continue
            elif command == "reset":
                if throws == 0:
                    print("Nie masz rundy do resetowania.")
                else:
                    throws -= 1
                    points_left = temp_score + throw_score
                    temp_score = points_left
                    print(f"Punkty: {temp_score}")
            else:
                print(con.wrong_throw)
                continue
    # score updating for next throw/round
    score_board.update({player: temp_score})
    print("\n")


# creating dict and flags
score_board = {}
playing = False

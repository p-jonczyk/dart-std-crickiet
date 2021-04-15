from crickiet_functions import create_players, crickiet_game, game_ends, player_crickiet_tab, player_name, player_score
from general_use_functions import exit_protocol
import constants as con


# main #####################################


def crickiet_main():
    print(con.menu_crickiet)

    # player creating
    while True:
        try:
            command =(input("Podaj ilość graczy: "))
            player_amount = int(command)
            if player_amount > 0:
                playing = True
            create_players(player_amount)
            print("\n")
            break
        except ValueError:
            if command == "exit":
                exit_protocol()
            else:
                print("Musisz podać liczbę graczy.")

    # game
    while playing == True:
        for i in range(con.rounds_crickiet + 1):
            if i < con.rounds_crickiet:
                print("\nRUNDA %d" % (i + 1))
                for j in range(player_amount):
                    print(f"{player_name(j + 1)} ({player_score(j + 1)}) -> {player_crickiet_tab(j + 1)}")
                print("\n")
                for k in range(player_amount):
                    crickiet_game(k + 1, player_amount)

            else:
                game_ends(player_amount)

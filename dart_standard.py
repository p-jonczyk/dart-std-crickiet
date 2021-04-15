from dart_standard_functions import *

# main #

def dart_main():
    print(con.menu_std)

    # player creating
    while True:
        try:
            command = (input("Podaj ilość graczy: "))
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
                continue

    # game
    while playing == True:
        for i in range(con.rounds_std + 1):
            if i < con.rounds_std:
                print("RUNDA %d" % (i + 1))
                for j in range(player_amount):
                    print(f"{player_name(j + 1)} -> {player_score(j + 1)}")
                print("\n")
                for k in range(player_amount):
                    throw(k + 1)
            else:
                print(f"Gra zakończona.\n")
                for j in range(player_amount):
                    print(f"{player_name(j + 1)} -> {player_score(j + 1)}\n")
                print(con.no_winner_msg_std)
                exit_protocol()

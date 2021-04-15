from crickiet import crickiet_main
from dart_standard import dart_main
from general_use_functions import exit_protocol
import constants as con

if __name__ == '__main__':
    print(con.menu_start)

    while True:
        command = input('Wybierz rodzaj gry: ').lower()
        if command == '1':
            dart_main()
            break
        elif command == '2':
            crickiet_main()
            break
        elif command == 'exit':
            exit_protocol()
            break
        else:
            print("Wybierz tryb gry...")

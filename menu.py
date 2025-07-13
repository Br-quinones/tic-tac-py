import msvcrt ; import keyboard ; import tictactoe ; import os ; import sys ; import time

########## Idioma #############
import traductor; global l
l = traductor.traductor_of_the_game()

def main_menu():
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"████████╗██╗ ██████╗            ████████╗ █████╗  ██████╗            ██████╗ ██╗   ██╗".center(115))
    print(f"╚══██╔══╝██║██╔════╝            ╚══██╔══╝██╔══██╗██╔════╝            ██╔══██╗╚██╗ ██╔╝".center(115))
    print(f"   ██║   ██║██║        █████╗      ██║   ███████║██║        █████╗   ██████╔╝ ╚████╔╝ ".center(115))
    print(f"   ██║   ██║██║        ╚════╝      ██║   ██╔══██║██║        ╚════╝   ██╔═══╝   ╚██╔╝  ".center(115))
    print(f"   ██║   ██║╚██████╗               ██║   ██║  ██║╚██████╗            ██║        ██║   ".center(115))
    print(f"   ╚═╝   ╚═╝ ╚═════╝               ╚═╝   ╚═╝  ╚═╝ ╚═════╝            ╚═╝        ╚═╝   ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                [1]{l.play}                [2]{l.languages}                [3]{l.credits}                [4]{l.exit}                ")#Ajuste idiomatico
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"        ███████                      ██      ██                        ███████        ".center(115))
    print(f"        ███████                      ██      ██                        ███████        ".center(115))
    print(f"        ███████    █                 ██      ██                   █    ███████        ".center(115))
    print(f"          ███    ████          ██████████████████████            ████    ███          ".center(115))
    print(f"          ███  █████                 ██      ██                   █████  ███          ".center(115))
    print(f"      ████████████                   ██      ██                     ████████████      ".center(115))
    print(f"     ███  ███                        ██      ██                          ███  ███     ".center(115))
    print(f"    ███   ███                  ██████████████████████                    ███   ███    ".center(115))
    print(f"     ███  ███                        ██      ██                          ███  ███     ".center(115))
    print(f"       ██ ███                        ██      ██                          ███ ██       ".center(115))
    print(f"          ███                        ██      ██                          ███          ".center(115))
    print(f"         ██████                                                        ██████         ".center(115))
    print(f"       ███    ███                                                    ███    ███       ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))
    while True:
        msvcrt.getch()
        choice = keyboard.read_key()
        if choice == "1":
            choice_for_play()
            break
        elif choice == "2":
            choice_for_language()
            break
        elif choice == "3":
            choice_for_credits()
            break
        elif choice == "4":
            choice_for_exit()
            break
        else:
            error_no_choice()

def choice_for_play():
    os.system("cls")
    tictactoe.the_game()

def choice_for_language():
    global l 
    global traductor

    os.system("cls")

    print("\n"*5)

    print(" " * 50 , "[1]Español" , "\n")
    print(" " * 50 , "[2]English" , "\n")
    print(" " * 50 , "[3]Nihongo" , "\n")
    print(" " * 50 , "[4]Portuguese" , "\n")
    print(" " * 50 , "[5]Français" , "\n")
    print(" " * 50 , "[6]Deutsch", "\n")

    msvcrt.getch()
    number_of_language = keyboard.read_key()
    if number_of_language == "1":
        traductor.main_language = "spanish"
        from languages import es as l
    elif number_of_language == "2":
        traductor.main_language = "english"
        from languages import en as l
    elif number_of_language == "3":
        traductor.main_language = "japanese"
        from languages import ja as l
    elif number_of_language == "4":
        traductor.main_language = "portuguese"
        from languages import pt as l
    elif number_of_language == "5":
        traductor.main_language = "france"
        from languages import fr as l
    elif number_of_language == "6":
        traductor.main_language = "germany"
        from languages import de as l
    
    os.system("cls")
    main_menu()

def choice_for_credits():
    os.system("cls")

    print("\n"*10)
    print(l.author.center(115))
    print(l.traductor.center(115))

    msvcrt.getch()
    os.system("cls")
    main_menu()

def choice_for_exit():
    os.system("cls")
    print("\n"*10)

    print(l.exiting.center(115))

    time.sleep(0.2)
    sys.exit()

def error_no_choice():
    print(l.invalid_key_error.center(115))
    time.sleep(0.25)
    os.system("cls")
    main_menu()

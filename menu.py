import msvcrt ; import keyboard ; import tictactoe ; import os ; import sys ; import time

########## Idioma #############
import variable; global l
l = variable.traductor_of_the_game()

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
    global variable

    os.system("cls")

    print("\n"*10)

    print(" "*50 , f"[1]{l.spanish}" , "\n")
    print(" "*50 , f"[2]{l.english}" , "\n")
    print(" "*50 , f"[3]{l.japanese}" , "\n")

    msvcrt.getch()
    number_of_language = keyboard.read_key()
    if number_of_language == "1":
        variable.main_language = "spanish"
        from languages import es as l
    elif number_of_language == "2":
        variable.main_language = "english"
        from languages import en as l
    elif number_of_language == "3":
        variable.main_language = "japanese"
        from languages import ja as l
    
    os.system("cls")
    main_menu()

def choice_for_credits():
    os.system("cls")

    print("\n"*10)
    print(" "*45 , l.author)
    print(" "*45 , l.traductor)

    msvcrt.getch()
    os.system("cls")
    main_menu()

def choice_for_exit():
    os.system("cls")
    print("\n"*10)

    print(" "*50 , l.exiting)

    time.sleep(0.2)
    sys.exit()

def error_no_choice():
    print(" "*45 , l.invalid_key_error)
    time.sleep(0.25)
    os.system("cls")
    main_menu()

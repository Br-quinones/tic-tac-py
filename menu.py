import msvcrt ; import keyboard ; import tictactoe ; import os ; import sys ; import time

########## Idioma #########

import variable
if variable.main_language == "spanish":
    import languages.es as l
elif variable.main_language == "english":
    import languages.en as l
elif variable.main_language == "japanese":
    import languages.ja as l

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
    print(f"     [1]{l.play}       [2]{l.languages}       [3]{l.credits}       [4]{l.exit}        ".center(115))
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
    print(l.choice_language.center(115))
    print(f"[1]{l.spanish}".center(115))
    print(f"[2]{l.english}".center(115))
    print(f"[3]{l.japanese}".center(115))

    msvcrt.getch()
    number_of_language = keyboard.read_key()
    if number_of_language == "1":
        variable.main_language = "spanish"
        from languages import es as l
    elif number_of_language == "2":
        variable.main_language = "english"
        from languages import en as l
    elif number_of_language == "3":
        variable.main_language == "japanese"
        from languages import ja as l
    
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
    print("Error caracter no valido".center(115))
    time.sleep(0.25)
    os.system("cls")
    main_menu()

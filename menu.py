import msvcrt ; import keyboard ; import os ; import sys ; import time
import the_game; import traductor
from colorama import Fore
global l
import sound
from languages import spansih as l

def main_menu():
    l = traductor.traductor_of_the_game()
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                {Fore.BLUE}████████╗██╗ ██████╗            {Fore.RED}████████╗ █████╗  ██████╗            {Fore.BLUE}██████╗ ██╗   ██╗{Fore.RESET}")
    print(f"                {Fore.BLUE}╚══██╔══╝██║██╔════╝            {Fore.RED}╚══██╔══╝██╔══██╗██╔════╝            {Fore.BLUE}██╔══██╗╚██╗ ██╔╝{Fore.RESET}")
    print(f"                {Fore.BLUE}   ██║   ██║██║        █████╗   {Fore.RED}   ██║   ███████║██║        █████╗   {Fore.BLUE}██████╔╝ ╚████╔╝ {Fore.RESET}")
    print(f"                {Fore.BLUE}   ██║   ██║██║        ╚════╝   {Fore.RED}   ██║   ██╔══██║██║        ╚════╝   {Fore.BLUE}██╔═══╝   ╚██╔╝  {Fore.RESET}")
    print(f"                {Fore.BLUE}   ██║   ██║╚██████╗            {Fore.RED}   ██║   ██║  ██║╚██████╗            {Fore.BLUE}██║        ██║   {Fore.RESET}")
    print(f"                {Fore.BLUE}   ╚═╝   ╚═╝ ╚═════╝            {Fore.RED}   ╚═╝   ╚═╝  ╚═╝ ╚═════╝            {Fore.BLUE}╚═╝        ╚═╝   {Fore.RESET}")
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                {Fore.GREEN}[1]{Fore.RESET}{l.play}                {Fore.GREEN}[2]{Fore.RESET}{l.languages}                {Fore.GREEN}[3]{Fore.RESET}{l.credits}                {Fore.GREEN}[4]{Fore.RESET}{l.exit}                ")#Ajuste idiomatico
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"                                                                                      ".center(115))
    print(f"        ███████                      ██      ██                        ███████        ".center(115))
    print(f"        ███████                      ██      ██                        ███████        ".center(115))
    print(f"        ███████    █                 ██      ██                   █    ███████        ".center(115))
    print(f"          ███    ████          ██████████████████████            ████    ███          ".center(115))
    print(f"                         ███  █████            {Fore.BLUE} ██ {Fore.RESET} ██ {Fore.RED}█  █{Fore.RESET} ██                   █████  ███          ")
    print(f"                     ████████████              {Fore.BLUE}█  █{Fore.RESET} ██ {Fore.RED} ██ {Fore.RESET} ██                     ████████████      ")
    print(f"                    ███  ███                   {Fore.BLUE} ██ {Fore.RESET} ██ {Fore.RED}█  █{Fore.RESET} ██                          ███  ███     ")
    print(f"    ███   ███                  ██████████████████████                    ███   ███    ".center(115))
    print(f"                    ███  ███                        ██ {Fore.BLUE} ██ {Fore.RESET} ██                          ███  ███     ")
    print(f"                      ██ ███                        ██ {Fore.BLUE}█  █{Fore.RESET} ██                          ███ ██       ")
    print(f"                         ███                        ██ {Fore.BLUE} ██ {Fore.RESET} ██                          ███          ")
    print(f"         ██████                                                        ██████         ".center(115))
    print(f"       ███    ███                                                    ███    ███       ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))
    print(f"      ███      ███                                                  ███      ███      ".center(115))

    while True:
        msvcrt.getch()
        choice = keyboard.read_key()

        sound.effect_sound("menu_01.wav")

        time.sleep(0.3)
        
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
    the_game.chapter_01()

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
        from languages import spansih as l
    elif number_of_language == "2":
        traductor.main_language = "english"
        from languages import english as l
    elif number_of_language == "3":
        traductor.main_language = "japanese"
        from languages import japanese as l
    elif number_of_language == "4":
        traductor.main_language = "portuguese"
        from languages import portuguese as l
    elif number_of_language == "5":
        traductor.main_language = "france"
        from languages import french as l
    elif number_of_language == "6":
        traductor.main_language = "germany"
        from languages import germany as l
    
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
    print(Fore.RED + l.invalid_key_error.center(115) + Fore.RESET)
    time.sleep(0.25)
    os.system("cls")
    main_menu()

import msvcrt ; import keyboard ; import os ; import sys ; import time #Librerias publicas
from colorama import Fore #Modulos publicos
import the_game; import traductor; import sound #Librerias privadas
from languages import spanish as l #Modulos privados

def main_menu():
    global l; l = traductor.traductor_of_the_game()
    os.system("cls")
    art_manu()

    while True:
        msvcrt.getch()
        choice = keyboard.read_key()
        
        if choice == "1":
            choice_for_play() ; break
        elif choice == "2":
            choice_for_language() ; break
        elif choice == "3":
            choice_for_credits() ; break
        elif choice == "4":
            choice_for_exit() ; break
        else:
            error_no_choice()

def art_manu():
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

def choice_for_play():
    sound.effect_sound("menu_01.wav")
    time.sleep(0.3)
    os.system("cls")
    if the_game.current_chapter == "chapter_01":
        the_game.chapter_01.history() 
    elif the_game.current_chapter == "chapter_02":
        the_game.chapter_02.history()
    elif the_game.current_chapter == "chapter_03":
        the_game.chapter_03.history()
    elif the_game.current_chapter == "chapter_04":
        the_game.chapter_04.history()
    elif the_game.current_chapter == "chapter_05":
        the_game.chapter_05.history()
    elif the_game.current_chapter == "chapter_06":
        the_game.chapter_06.history()
    
def choice_for_language():
    global l 
    global traductor

    sound.effect_sound("menu_01.wav")
    time.sleep(0.3)
    
    os.system("cls")

    print("\n"*5)

    print("Seleccione su idioma".center(115))
    print("\n")

    print("[1]Español   ".center(115))
    print("[2]English   ".center(115))
    print("[3]Nihongo   ".center(115))
    print("[4]Portuguese".center(115))
    print("[5]Français  ".center(115))
    print("[6]Deutsch   ".center(115))

    msvcrt.getch()
    number_of_language = keyboard.read_key()
    if number_of_language == "1":
        traductor.main_language = "spanish"
    elif number_of_language == "2":
        traductor.main_language = "english"
    elif number_of_language == "3":
        traductor.main_language = "japanese"
    elif number_of_language == "4":
        traductor.main_language = "portuguese"
    elif number_of_language == "5":
        traductor.main_language = "france"
    elif number_of_language == "6":
        traductor.main_language = "germany"
    
    os.system("cls")
    main_menu()

def choice_for_credits():
    sound.effect_sound("menu_01.wav")
    time.sleep(0.3)

    os.system("cls")
    print("\n"*10)

    print(l.author.center(115))
    print(l.traductor.center(115))

    msvcrt.getch()

    os.system("cls")
    main_menu()

def choice_for_exit():
    sound.effect_sound("menu_01.wav")
    time.sleep(0.3)
    
    print(l.exiting.center(115))

    time.sleep(0.2)
    sys.exit()

def error_no_choice():
    sound.effect_sound("error.wav")
    print(Fore.RED + l.invalid_key_error.center(115) + Fore.RESET)
    time.sleep(0.25)
    os.system("cls")
    main_menu()
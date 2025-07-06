import msvcrt ; import keyboard ; import tictactoe ; import os ; import sys ; import time
import constants

def main_menu():
    print("                                                                                      ".center(115))
    print("                                                                                      ".center(115))
    print("████████╗██╗ ██████╗            ████████╗ █████╗  ██████╗            ██████╗ ██╗   ██╗".center(115))
    print("╚══██╔══╝██║██╔════╝            ╚══██╔══╝██╔══██╗██╔════╝            ██╔══██╗╚██╗ ██╔╝".center(115))
    print("   ██║   ██║██║        █████╗      ██║   ███████║██║        █████╗   ██████╔╝ ╚████╔╝ ".center(115))
    print("   ██║   ██║██║        ╚════╝      ██║   ██╔══██║██║        ╚════╝   ██╔═══╝   ╚██╔╝  ".center(115))
    print("   ██║   ██║╚██████╗               ██║   ██║  ██║╚██████╗            ██║        ██║   ".center(115))
    print("   ╚═╝   ╚═╝ ╚═════╝               ╚═╝   ╚═╝  ╚═╝ ╚═════╝            ╚═╝        ╚═╝   ".center(115))
    print("                                                                                      ".center(115))
    print("                                                                                      ".center(115))
    print(" [1] Jugar             [2] Idioma             [3] Creditos           [4] Salir        ".center(115))
    print("                                                                                      ".center(115))
    print("                                                                                      ".center(115))
    print("                                                                                      ".center(115))
    print("        ███████                      ██      ██                        ███████        ".center(115))
    print("        ███████                      ██      ██                        ███████        ".center(115))
    print("        ███████    █                 ██      ██                   █    ███████        ".center(115))
    print("          ███    ████          ██████████████████████            ████    ███          ".center(115))
    print("          ███  █████                 ██      ██                   █████  ███          ".center(115))
    print("      ████████████                   ██      ██                     ████████████      ".center(115))
    print("     ███  ███                        ██      ██                          ███  ███     ".center(115))
    print("    ███   ███                  ██████████████████████                    ███   ███    ".center(115))
    print("     ███  ███                        ██      ██                          ███  ███     ".center(115))
    print("       ██ ███                        ██      ██                          ███ ██       ".center(115))
    print("          ███                        ██      ██                          ███          ".center(115))
    print("         ██████                                                        ██████         ".center(115))
    print("       ███    ███                                                    ███    ███       ".center(115))
    print("      ███      ███                                                  ███      ███      ".center(115))
    print("      ███      ███                                                  ███      ███      ".center(115))
    print("      ███      ███                                                  ███      ███      ".center(115))

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
    os.system("cls")
    print("\n"*10)
    print("Seleccione su idioma: ".center(115))
    print(" -Español".center(115))
    print(" -English".center(115))
    msvcrt.getch()
    os.system("cls")
    main_menu()

def choice_for_credits():
    os.system("cls")
    print("\n"*10)
    print("Author: Br_Quinones".center(115))
    print("Support: Chat GPT".center(115))
    print("Traductor: Gemeni".center(115))
    msvcrt.getch()
    os.system("cls")
    main_menu()

def choice_for_exit():
    os.system("cls")
    print("\n"*10)
    print("Saliendo...".center(115))
    time.sleep(0.3)
    sys.exit()

def error_no_choice():
    print("Error caracter no valido".center(115))
    time.sleep(0.5)
    os.system("cls")
    main_menu()

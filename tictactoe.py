######### Instalar librerias y colocar constantes#############
import os; import time
from colorama import Fore, Style
import msvcrt; import keyboard
import random

print(Style.BRIGHT ,end="")

############ Graficos ##################

#Zero
zero_1 = Fore.BLUE + "  ████  " + Fore.RESET
zero_2 = Fore.BLUE + " ██  ██ " + Fore.RESET 
zero_3 = Fore.BLUE + "  ████  " + Fore.RESET

#Equis
equis_1 = Fore.RED + " ██  ██ " + Fore.RESET
equis_2 = Fore.RED + "   ██   " + Fore.RESET
equis_3 = Fore.RED + " ██  ██ " + Fore.RESET

#Vacio
empty = Fore.BLACK + "        " + Fore.RESET 

#Vacio con numero
empty_01 = Fore.GREEN + "   01   " + Fore.RESET
empty_02 = Fore.GREEN + "   02   " + Fore.RESET 
empty_03 = Fore.GREEN + "   03   " + Fore.RESET 
empty_04 = Fore.GREEN + "   04   " + Fore.RESET 
empty_05 = Fore.GREEN + "   05   " + Fore.RESET 
empty_06 = Fore.GREEN + "   06   " + Fore.RESET 
empty_07 = Fore.GREEN + "   07   " + Fore.RESET 
empty_08 = Fore.GREEN + "   08   " + Fore.RESET 
empty_09 = Fore.GREEN + "   09   " + Fore.RESET 

########## Colocar vacio a todos ###########

tic_1a = empty ; tic_1b = empty_01 ; tic_1c = empty
tic_2a = empty ; tic_2b = empty_02 ; tic_2c = empty
tic_3a = empty ; tic_3b = empty_03 ; tic_3c = empty
tic_4a = empty ; tic_4b = empty_04 ; tic_4c = empty
tic_5a = empty ; tic_5b = empty_05 ; tic_5c = empty
tic_6a = empty ; tic_6b = empty_06 ; tic_6c = empty
tic_7a = empty ; tic_7b = empty_07 ; tic_7c = empty
tic_8a = empty ; tic_8b = empty_08 ; tic_8c = empty
tic_9a = empty ; tic_9b = empty_09 ; tic_9c = empty

############ listas ######################### 

valid_numbers = ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]
selected_numbers = []

############## Union de graficos ###############
def graphic_tictactoe():
    os.system("cls")
    print(f"")
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"██{tic_7a}██  ██{tic_8a}██  ██{tic_9a}██".center(145))
    print(f"██{tic_7b}██  ██{tic_8b}██  ██{tic_9b}██".center(145))
    print(f"██{tic_7c}██  ██{tic_8c}██  ██{tic_9c}██".center(145))
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"")
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"██{tic_4a}██  ██{tic_5a}██  ██{tic_6a}██".center(145))
    print(f"██{tic_4b}██  ██{tic_5b}██  ██{tic_6b}██".center(145))
    print(f"██{tic_4c}██  ██{tic_5c}██  ██{tic_6c}██".center(145))
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"")
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"██{tic_1a}██  ██{tic_2a}██  ██{tic_3a}██".center(145))
    print(f"██{tic_1b}██  ██{tic_2b}██  ██{tic_3b}██".center(145))
    print(f"██{tic_1c}██  ██{tic_2c}██  ██{tic_3c}██".center(145))
    print(f"████████████  ████████████  ████████████".center(115))
    print(f"\n" + Fore.GREEN)
    print(f"_______████████████████████████████████████████████_______".center(115))
    print(f"")
    print(f" TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA ".center(115))
    print(Fore.RESET,end="")
    print("███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████".center(115))
    print("█  █  █   █ ███ █   █ ███ █   █ █ █ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █".center(115))
    print("█ ██  █   █   █ █   █   █ █   █ █ █ █   █ █   █   █ █   █   █   █ █   █ █ █ █   █ █ █ █".center(115))
    print("█  █  █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █  █  █   █ ███ █   █ ███ █".center(115))
    print("█  █  █   █ █   █   █   █ █   █   █ █   █   █ █   █ █ █ █   █  █  █   █ █ █ █   █   █ █".center(115))
    print("█  █  █   █ ███ █   █ ███ █   █   █ █   █ ███ █   █ ███ █   █  █  █   █ ███ █   █   █ █".center(115))
    print("███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████".center(115))

########### Colocar zero ##################
def Human_turn():
    global tic_1a , tic_1b , tic_1c
    global tic_2a , tic_2b , tic_2c
    global tic_3a , tic_3b , tic_3c
    global tic_4a , tic_4b , tic_4c
    global tic_5a , tic_5b , tic_5c
    global tic_6a , tic_6b , tic_6c
    global tic_7a , tic_7b , tic_7c
    global tic_8a , tic_8b , tic_8c
    global tic_9a , tic_9b , tic_9c
    global selected_numbers
    
    while True:
        msvcrt.getch()
        key = keyboard.read_key()
        if key in valid_numbers and key not in selected_numbers:
            selected_numbers.append(key) ; break
        else:
            print("Numero no valido".center(115))
    
    if key == "1":
        tic_1a = zero_1 ; tic_1b = zero_2 ; tic_1c = zero_3
    elif key == "2":
        tic_2a = zero_1 ; tic_2b = zero_2 ; tic_2c = zero_3
    elif key == "3":
        tic_3a = zero_1 ; tic_3b = zero_2 ;tic_3c = zero_3
    elif key == "4":
        tic_4a = zero_1 ; tic_4b = zero_2 ; tic_4c = zero_3
    elif key == "5":
        tic_5a = zero_1 ; tic_5b = zero_2 ; tic_5c = zero_3
    elif key == "6":
        tic_6a = zero_1 ; tic_6b = zero_2 ; tic_6c = zero_3
    elif key == "7":
        tic_7a = zero_1 ; tic_7b = zero_2 ; tic_7c = zero_3
    elif key == "8":
        tic_8a = zero_1 ; tic_8b = zero_2 ; tic_8c = zero_3
    elif key == "9":
        tic_9a = zero_1 ; tic_9b = zero_2 ; tic_9c = zero_3

########## Colocar equis #################
def machine_turn():
    global tic_1a , tic_1b , tic_1c
    global tic_2a , tic_2b , tic_2c
    global tic_3a , tic_3b , tic_3c
    global tic_4a , tic_4b , tic_4c
    global tic_5a , tic_5b , tic_5c
    global tic_6a , tic_6b , tic_6c
    global tic_7a , tic_7b , tic_7c
    global tic_8a , tic_8b , tic_8c
    global tic_9a , tic_9b , tic_9c
    global selected_numbers

    print(Fore.GREEN +  "\n" + "Enemigo pensando...".center(115) + Fore.RESET)
    time.sleep(1) 

    while True:
        random_number = str(random.randint(1,9))
        if random_number not in selected_numbers:
            selected_numbers.append(random_number)
            break
    
    if random_number == "1":
        tic_1a = equis_1 ; tic_1b = equis_2 ; tic_1c = equis_3
    elif random_number == "2":
        tic_2a = equis_1 ; tic_2b = equis_2 ; tic_2c = equis_3
    elif random_number == "3":
        tic_3a = equis_1 ; tic_3b = equis_2 ;tic_3c = equis_3
    elif random_number == "4":
        tic_4a = equis_1 ; tic_4b = equis_2 ; tic_4c = equis_3
    elif random_number == "5":
        tic_5a = equis_1 ; tic_5b = equis_2 ; tic_5c = equis_3
    elif random_number == "6":
        tic_6a = equis_1 ; tic_6b = equis_2 ; tic_6c = equis_3
    elif random_number == "7":
        tic_7a = equis_1 ; tic_7b = equis_2 ; tic_7c = equis_3
    elif random_number == "8":
        tic_8a = equis_1 ; tic_8b = equis_2 ; tic_8c = equis_3
    elif random_number == "9":
        tic_9a = equis_1 ; tic_9b = equis_2 ; tic_9c = equis_3

##########3 Aqui el juego ############
def the_game():
    while True:
        graphic_tictactoe()
        Human_turn()
        graphic_tictactoe()
        machine_turn()
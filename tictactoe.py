######### Instalar librerias y colocar constantes#############
import os; import time
from colorama import Fore, Style
import msvcrt; import keyboard
import random

print(Style.BRIGHT ,end="")

argumento1 = 145
argumento2 = 115
argumento3 = 57

############ Graficos ##################

zero_1 = Fore.BLUE + "  ████  " + Fore.RESET
zero_2 = Fore.BLUE + " ██  ██ " + Fore.RESET 
zero_3 = Fore.BLUE + "  ████  " + Fore.RESET

equis_1 = Fore.RED + " ██  ██ " + Fore.RESET
equis_2 = Fore.RED + "   ██   " + Fore.RESET
equis_3 = Fore.RED + " ██  ██ " + Fore.RESET

empty = Fore.BLACK + "        " + Fore.RESET 

empty_01 = Fore.GREEN + "   01   " + Fore.RESET
empty_02 = Fore.GREEN + "   02   " + Fore.RESET 
empty_03 = Fore.GREEN + "   03   " + Fore.RESET 
empty_04 = Fore.GREEN + "   04   " + Fore.RESET 
empty_05 = Fore.GREEN + "   05   " + Fore.RESET 
empty_06 = Fore.GREEN + "   06   " + Fore.RESET 
empty_07 = Fore.GREEN + "   07   " + Fore.RESET 
empty_08 = Fore.GREEN + "   08   " + Fore.RESET 
empty_09 = Fore.GREEN + "   09   " + Fore.RESET 

valid_numbers = ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]
selected_numbers = []

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

########### Colocar zero ##################

def choice_key():
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
        if key in valid_numbers:
            if key in selected_numbers:
                print("Lugar ya elegido!".center(argumento2))
                time.sleep(1)
                os.system("cls")
                the_game()
            else:
                ## Aqui agregar la funcion de iluminacion ##
                selected_numbers.append(key)
                break
        else:
            print("Numero no valido".center(argumento2))
            time.sleep(1)
            os.system("cls")
            the_game()
            
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
def choice_key_ai():
    global tic_1a , tic_1b , tic_1c
    global tic_2a , tic_2b , tic_2c


    random_number = str(random.randint(1,2))
    
    if random_number == "1":
        tic_1a = equis_1 ; tic_1b = equis_2 ; tic_1c = equis_3
    elif random_number == "2":
        tic_2a = equis_1 ;  tic_2b = equis_2 ; tic_2c = equis_3

    the_game()


    

############## El juego ###############
def the_game():
    while True:
        os.system("cls")
        print(f"")
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_7a}██  ██{tic_8a}██  ██{tic_9a}██".center(argumento1))
        print(f"██{tic_7b}██  ██{tic_8b}██  ██{tic_9b}██".center(argumento1))
        print(f"██{tic_7c}██  ██{tic_8c}██  ██{tic_9c}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"")
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_4a}██  ██{tic_5a}██  ██{tic_6a}██".center(argumento1))
        print(f"██{tic_4b}██  ██{tic_5b}██  ██{tic_6b}██".center(argumento1))
        print(f"██{tic_4c}██  ██{tic_5c}██  ██{tic_6c}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"")
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_1a}██  ██{tic_2a}██  ██{tic_3a}██".center(argumento1))
        print(f"██{tic_1b}██  ██{tic_2b}██  ██{tic_3b}██".center(argumento1))
        print(f"██{tic_1c}██  ██{tic_2c}██  ██{tic_3c}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(Fore.GREEN)
        print("_______████████████████████████████████████████████_______".center(argumento2))
        print("")
        print(" TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA     TECLA ".center(argumento2))
        print(Fore.RESET,end="")
        print("███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████".center(argumento2))
        print("█  █  █   █ ███ █   █ ███ █   █ █ █ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █".center(argumento2))
        print("█ ██  █   █   █ █   █   █ █   █ █ █ █   █ █   █   █ █   █   █   █ █   █ █ █ █   █ █ █ █".center(argumento2))
        print("█  █  █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █ ███ █   █  █  █   █ ███ █   █ ███ █".center(argumento2))
        print("█  █  █   █ █   █   █   █ █   █   █ █   █   █ █   █ █ █ █   █  █  █   █ █ █ █   █   █ █".center(argumento2))
        print("█  █  █   █ ███ █   █ ███ █   █   █ █   █ ███ █   █ ███ █   █  █  █   █ ███ █   █   █ █".center(argumento2))
        print("███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████   ███████".center(argumento2))
        
        choice_key()
        choice_key_ai()

        os.system("cls")
        


##Actualizar variables y agregar botones de referencia jsjsjs
    
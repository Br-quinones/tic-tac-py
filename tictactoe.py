#Pantalla completa y zoom
if __name__ == '__main__':
    import time; import keyboard 

    keyboard.press_and_release("f11")
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)

######### Instalar librerias y colocar constantes#############
import os
from colorama import Fore, Style

print(Style.BRIGHT ,end="")

argumento1 = 145
argumento2 = 115

############ Graficos ##################

zero_1 = Fore.RED + "  ████  " + Fore.RESET
zero_2 = Fore.RED + " ██  ██ " + Fore.RESET 
zero_3 = Fore.RED + "  ████  " + Fore.RESET

equis_1 = Fore.BLUE + " ██  ██ " + Fore.RESET
equis_2 = Fore.BLUE + "   ██   " + Fore.RESET
equis_3 = Fore.BLUE + " ██  ██ " + Fore.RESET

empty = Fore.BLACK + "        " + Fore.RESET 

########## Colocar vacio a todos ###########

tic_a1 = empty
tic_a2 = empty
tic_a3 = empty
tic_b1 = empty
tic_b2 = empty
tic_b3 = empty
tic_c1 = empty
tic_c2 = empty
tic_c3 = empty
tic_d1 = empty
tic_d2 = empty
tic_d3 = empty
tic_e1 = empty
tic_e2 = empty
tic_e3 = empty
tic_f1 = empty
tic_f2 = empty
tic_f3 = empty
tic_g1 = empty
tic_g2 = empty
tic_g3 = empty
tic_h1 = empty
tic_h2 = empty
tic_h3 = empty
tic_i1 = empty
tic_i2 = empty
tic_i3 = empty

########### Colocar zero ##################

def choice_coordinate():
    global tic_a1 , tic_a2 , tic_a3
    global tic_b1 , tic_b2 , tic_b3
    global tic_c1 , tic_c2 , tic_c3
    global tic_d1 , tic_d2 , tic_d3
    global tic_e1 , tic_e2 , tic_e3
    global tic_f1 , tic_f2 , tic_f3
    global tic_g1 , tic_g2 , tic_g3
    global tic_h1 , tic_h2 , tic_h3
    global tic_i1 , tic_i2 , tic_i3
    
    coordinate = input("Elige la letra [a,b,c...i]: ")

    if coordinate == "a":
        tic_a1 = zero_1
        tic_a2 = zero_2
        tic_a3 = zero_3
    elif coordinate == "b":
        tic_b1 = zero_1
        tic_b2 = zero_2
        tic_b3 = zero_3
    elif coordinate == "c":
        tic_c1 = zero_1
        tic_c2 = zero_2
        tic_c3 = zero_3
    elif coordinate == "d":
        tic_d1 = zero_1
        tic_d2 = zero_2
        tic_d3 = zero_3
    elif coordinate == "e":
        tic_e1 = zero_1
        tic_e2 = zero_2
        tic_e3 = zero_3
    elif coordinate == "f":
        tic_f1 = zero_1
        tic_f2 = zero_2
        tic_f3 = zero_3
    elif coordinate == "g":
        tic_g1 = zero_1
        tic_g2 = zero_2
        tic_g3 = zero_3
    elif coordinate == "h":
        tic_h1 = zero_1
        tic_h2 = zero_2
        tic_h3 = zero_3
    elif coordinate == "i":
        tic_i1 = zero_1
        tic_i2 = zero_2
        tic_i3 = zero_3

############## El juego ###############
def the_game():
    while True:
        print("\n")
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_a1}██  ██{tic_b1}██  ██{tic_c1}██".center(argumento1))
        print(f"██{tic_a2}██  ██{tic_b2}██  ██{tic_c2}██".center(argumento1))
        print(f"██{tic_a3}██  ██{tic_b3}██  ██{tic_c3}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"                                        ".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_d1}██  ██{tic_e1}██  ██{tic_f1}██".center(argumento1))
        print(f"██{tic_d2}██  ██{tic_e2}██  ██{tic_f2}██".center(argumento1))
        print(f"██{tic_d3}██  ██{tic_e3}██  ██{tic_f3}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"                                        ".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print(f"██{tic_g1}██  ██{tic_h1}██  ██{tic_i1}██".center(argumento1))
        print(f"██{tic_g2}██  ██{tic_h2}██  ██{tic_i2}██".center(argumento1))
        print(f"██{tic_g3}██  ██{tic_h3}██  ██{tic_i3}██".center(argumento1))
        print(f"████████████  ████████████  ████████████".center(argumento2))
        print("                                         ".center(argumento1))
        print("_______████████████████████████████████████████████_______".center(argumento2))

        choice_coordinate()

        os.system("cls")
    
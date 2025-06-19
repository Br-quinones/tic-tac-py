#Pantalla completa y zoom
if __name__ == '__main__':
    import time; import keyboard 

    keyboard.press_and_release("f11")
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)

######### Instalar librerias y colocar constantes#############
import os; import time
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

empty_01 = Fore.GREEN + "   01   " + Fore.RESET
empty_02 = Fore.GREEN + "   02   " + Fore.RESET 
empty_03 = Fore.GREEN + "   03   " + Fore.RESET 
empty_04 = Fore.GREEN + "   04   " + Fore.RESET 
empty_05 = Fore.GREEN + "   05   " + Fore.RESET 
empty_06 = Fore.GREEN + "   06   " + Fore.RESET 
empty_07 = Fore.GREEN + "   07   " + Fore.RESET 
empty_08 = Fore.GREEN + "   08   " + Fore.RESET 
empty_09 = Fore.GREEN + "   09   " + Fore.RESET 

listo = ["1","2","3","4","5","6","7","8","9","01","02","03","04","05","06","07","08","09"]
lista = []
########## Colocar vacio a todos ###########

tic_a1 = empty ; tic_a2 = empty_01 ;tic_a3 = empty
tic_b1 = empty ; tic_b2 = empty_02 ; tic_b3 = empty
tic_c1 = empty ; tic_c2 = empty_03 ; tic_c3 = empty
tic_d1 = empty ; tic_d2 = empty_04 ; tic_d3 = empty
tic_e1 = empty ; tic_e2 = empty_05 ; tic_e3 = empty
tic_f1 = empty ; tic_f2 = empty_06 ; tic_f3 = empty
tic_g1 = empty ; tic_g2 = empty_07 ; tic_g3 = empty
tic_h1 = empty ; tic_h2 = empty_08 ; tic_h3 = empty
tic_i1 = empty ; tic_i2 = empty_09 ; tic_i3 = empty

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
    global lista
    
    while True:
        coordinate = input("Elige el numero 1/2/3/.../9: ")
        if coordinate in listo:
            if coordinate in lista:
                print("Lugar ya elegido!")
                time.sleep(1)
                os.system("cls")
                the_game()
            else:
                lista.append(coordinate)
                break
        else:
            print("Numero no valido")
            time.sleep(1)
            os.system("cls")
            the_game()
            
    if coordinate == "1":
        tic_a1 = zero_1
        tic_a2 = zero_2
        tic_a3 = zero_3
    elif coordinate == "2":
        tic_b1 = zero_1
        tic_b2 = zero_2
        tic_b3 = zero_3
    elif coordinate == "3":
        tic_c1 = zero_1
        tic_c2 = zero_2
        tic_c3 = zero_3
    elif coordinate == "4":
        tic_d1 = zero_1
        tic_d2 = zero_2
        tic_d3 = zero_3
    elif coordinate == "5":
        tic_e1 = zero_1
        tic_e2 = zero_2
        tic_e3 = zero_3
    elif coordinate == "6":
        tic_f1 = zero_1
        tic_f2 = zero_2
        tic_f3 = zero_3
    elif coordinate == "7":
        tic_g1 = zero_1
        tic_g2 = zero_2
        tic_g3 = zero_3
    elif coordinate == "8":
        tic_h1 = zero_1
        tic_h2 = zero_2
        tic_h3 = zero_3
    elif coordinate == "9":
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
        print(Fore.GREEN + "_______████████████████████████████████████████████_______".center(argumento2) + Fore.RESET)

        choice_coordinate()

        os.system("cls")
    
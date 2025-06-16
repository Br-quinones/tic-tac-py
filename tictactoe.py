import msvcrt
from colorama import Fore, Style

print(Style.BRIGHT ,end="")

def jsjs():
    varibale = "o"
    if varibale == "x":
        equia1 = Fore.BLUE + " ██  ██ " + Fore.RESET
        equia2 = Fore.BLUE + "   ██   " + Fore.RESET
        equia3 = Fore.BLUE + " ██  ██ " + Fore.RESET

    elif varibale == "o":
        equia1 = Fore.RED + "  ████  " + Fore.RESET
        equia2 = Fore.RED + " ██  ██ " + Fore.RESET 
        equia3 = Fore.RED + "  ████  " + Fore.RESET

    #tic_a1

    argumento1 = 145
    argumento2 = 115
    
    print("\n")
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print(f"██{equia1}██  ██{equia1}██  ██{equia1}██".center(argumento1))
    print(f"██{equia2}██  ██{equia2}██  ██{equia2}██".center(argumento1))
    print(f"██{equia3}██  ██{equia3}██  ██{equia3}██".center(argumento1))
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print(f"                                        ".center(argumento1))
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print(f"██{equia1}██  ██{equia1}██  ██{equia1}██".center(argumento1))
    print(f"██{equia2}██  ██{equia2}██  ██{equia2}██".center(argumento1))
    print(f"██{equia3}██  ██{equia3}██  ██{equia3}██".center(argumento1))
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print(f"                                        ".center(argumento1))
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print(f"██{equia1}██  ██{equia1}██  ██{equia1}██".center(argumento1))
    print(f"██{equia2}██  ██{equia2}██  ██{equia2}██".center(argumento1))
    print(f"██{equia3}██  ██{equia3}██  ██{equia3}██".center(argumento1))
    print(f"████████████  ████████████  ████████████".center(argumento2))
    print("                                         ".center(argumento1))
    print("_______████████████████████████████████████████████_______".center(argumento2))
    msvcrt.getch()
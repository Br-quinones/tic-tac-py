import sys; import json; import time
import msvcrt
from colorama import Fore

#Abrir .json para idiomas 
with open("languages/spanish.json", "r", encoding="utf-8") as file:
    languages = json.load(file)

def deletreo(word):
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")
    msvcrt.getch()

class dialogue:
    def mia(message):
        print(Fore.GREEN + "Mia: " + Fore.RESET ,end="")
        deletreo(message)

dialogue.mia("En un lugar de la mancha de cuyo nombre no quiero recordar no ha mucho tiempo")
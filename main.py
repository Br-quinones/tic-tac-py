#Liberias
import time; import keyboard ; import json
from colorama import Style; import sys

#Cargando programa
keyboard.press_and_release("f11")
for _ in range(8):
    keyboard.press_and_release("ctrl+plus")
    time.sleep(0.01)

#Json para idiomas 
with open("lang.json", "r", encoding="utf-8") as file:
    languages = json.load(file)

#Aplicar brillo a 
print(Style.BRIGHT,end="")

def deletreo(message):
    for letra in message:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")
    input()





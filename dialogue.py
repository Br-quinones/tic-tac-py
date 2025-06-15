import sys; import json; import time

#Abrir .json para idiomas 
with open("lang.json", "r", encoding="utf-8") as file:
    languages = json.load(file)

def deletreo(message):
    for letra in message:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")
    input()
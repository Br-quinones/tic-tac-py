import sys; import json; import time
import msvcrt; import art
from colorama import Fore
import os

#Abrir .json para idiomas 
with open("languages/spanish.json", "r", encoding="utf-8") as file:
    languages = json.load(file)

def deletreo(word):
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.015)
    msvcrt.getch()
    os.system("cls")

class message:
    def agatha(text):
        art.agatha_art()
        print(Fore.GREEN + "Agatha: " + Fore.RESET ,end="")
        deletreo(text)

    def beatrice(text):
        art.beatrice_art()
        print(Fore.MAGENTA + "Beatriz: " + Fore.RESET ,end="")
        deletreo(text)

    def victoria(text):
        art.victoria_art()
        print(Fore.YELLOW + "Victoria: " + Fore.RESET ,end="")
        deletreo(text)

def chapter_01():
    message.agatha("En los reinos de antaño, donde la niebla danzaba entre los robles milenarios...")
    message.victoria("¿Agatha, qué fantasías recitas ahora?")
    message.agatha("Oh, solo me inspiro en un tomo antiguo que encontré, Victoria.")
    message.beatrice("¡Basta de poesía! ¡Tenemos que entrenar nuestras mentes! ¡A jugar, ya!")
    message.agatha("Muy bien, Beatrice. ¡El desafío ha sido lanzado!")
    message.victoria("Espera, Agatha, permíteme explicarte las mecánicas básicas de este juego en tu dispositivo...")
    message.beatrice("¡Tonterías! ¡No hay tiempo para tutoriales! ¡La verdadera maestría se forja en el fragor de la batalla!")
    message.beatrice("Además, la derrota contundente es la mejor lección, ¿no crees?")
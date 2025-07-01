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
        art.agatha_ascci()
        print(Fore.GREEN + "Agatha: " + Fore.RESET ,end="")
        deletreo(text)

    def beatrice(text):
        art.beatrice_ascci()
        print(Fore.MAGENTA + "Beatriz: " + Fore.RESET ,end="")
        deletreo(text)

    def victoria(text):
        art.victoria_ascci()
        print(Fore.YELLOW + "Victoria: " + Fore.RESET ,end="")
        deletreo(text)

    def director(text):
        art.directo_ascci()
        print(Fore.RED + "Director: " + Fore.RESET ,end="")
        deletreo(text)

def chapter_01():
    message.director("Jugador este juego solo funciona su teclado.")
    message.director("Presione la tecla Espace para pasar en dialogo y dialogo y su teclas con numeros para jugar el 3 en raya")
    message.director("Bueno despues de interrumpirlo siga con al historia.")
    message.agatha("En los reinos de antaño, donde la niebla danzaba entre los robles...")
    message.victoria("¿Agatha, qué fantasías recitas?")
    message.agatha("Oh, solo me inspiro en un tomo antiguo que encontré.")
    message.beatrice("¡Basta de poesía! ¡Tenemos que entrenar nuestras mentes! ¡A jugar, ya!")
    message.agatha("Muy bien, Beatrice. Pero yo no se jugar esto")
    message.victoria("Espera, Agatha, permíteme explicarte las mecánicas básicas de este juego...")
    message.beatrice("¡Tonterías! ¡No hay tiempo para tutoriales! !A pura paliza aprenderas a jugar!")
    message.agatha("Ehhh, pero explicame gano o pierdo...")
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
    message.agatha("En un lugar de la Mancha, de cuyo nombre no quiero acordarme.")
    message.victoria("¿Pero que estas hablando mujer?")
    message.agatha("Oh tan solo estaba leyendo un libro que encontre.")
    message.beatrice("Hey si dejan de perder el tiempo con libros y entrenamos.")
    message.agatha("Bien beatrice, entrenemos entonces")
    message.victoria("Bueno Agatha, te explico como funciona el juego, usando tu teclado físico...")
    message.beatrice("Ahhh, panplinas el juego es tan facil, vamos de frente a la acción.")
    message.beatrice("Ademas la mejor forma de aprender es mediante la paliza.")
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
        time.sleep(0.02)
    print("\n")
    msvcrt.getch()

class message:
    def agatha(text):
        print(Fore.GREEN + "Agatha: " + Fore.RESET ,end="")
        deletreo(text)

    def beatriz(text):
        print(Fore.MAGENTA + "Beatriz: " + Fore.RESET ,end="")
        deletreo(text)

    def victoria(text):
        print(Fore.YELLOW + "Victoria: " + Fore.RESET ,end="")
        deletreo(text)


def chapter_01():
    message.agatha("En un lugar de la mancha de cuyo nombre no quiero recordar no ha mucho tiempo")
    message.victoria("¿Pero que estas hablando mujer?")
    message.agatha("Oh tan solo estaba leyendo un buen libro que encontre")
    message.beatriz("Hey si dejamos de perder nuestro tiempo con libros y entrenamos")
    message.agatha("Si mejor, dejare esto a un lado por un momento")
    message.victoria("Agatha te explico como funciona juego")
    message.beatriz("Panplinas el juego es tan facil, vamos de frente a la acción.")
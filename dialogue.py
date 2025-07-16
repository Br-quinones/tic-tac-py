import sys; import json; import time
import msvcrt; import art
from colorama import Fore
import os

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

    def role(text):
        art.role_ascci()
        print(Fore.CYAN + "Roleo: " + Fore.RESET , end="")
        deletreo(text)

import tictactoe
def chapter_01():
    message.role("Observas que dentro de una salón una muchedumbre rodea algo.")
    message.role("Ese algo no es más que una intensa partida del 3 en raya entre dos chicas")
    message.victoria("Otra persona aplastada, por mi gran equipo!")
    message.victoria("Oye tu, si tu él que acaba de llegar ¿una ronda que dices?")
    message.agatha("Victoria... dejame practicar, esta persona tambien es principiante a igual que yo")
    message.victoria("pufff, bueno practica entonces")
    tictactoe.the_game("easy")

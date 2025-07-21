import sys; import time; import os
import msvcrt; import art
from colorama import Fore
from pygame import mixer 
import sound

def deletreo(words, loop):
    sound.loop_sound(loop)
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.015)
    mixer.Channel(2).stop()
    msvcrt.getch()
    os.system("cls")

class message:
    def agatha(text):
        art.agatha_ascci()
        print(Fore.GREEN + "Agatha: " + Fore.RESET ,end="")
        deletreo(text, "bleep001.ogg")

    def beatrice(text):
        art.beatrice_ascci()
        print(Fore.MAGENTA + "Beatriz: " + Fore.RESET ,end="")
        deletreo(text, "bleep002.ogg")

    def victoria(text):
        art.victoria_ascci()
        print(Fore.YELLOW + "Victoria: " + Fore.RESET ,end="")
        deletreo(text, "bleep005.ogg")

    def director(text):
        art.directo_ascci()
        print(Fore.RED + "Director: " + Fore.RESET ,end="")
        deletreo(text, "bleep004.ogg")

    def role(text):
        art.role_ascci()
        print(Fore.CYAN + "Roleo: " + Fore.RESET , end="")
        deletreo(text, "bleep003.ogg")
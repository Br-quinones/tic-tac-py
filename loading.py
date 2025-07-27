from pygame import mixer
from colorama import Style
import os
import sound

def init_game():
    print("...".center(115)) #Aqui podria ir unos hilos, al final de proyecto se observara
    print(Style.BRIGHT)
    mixer.init()
    sound.music_sound("the_last_of_us.mp3")
    os.system("cls")
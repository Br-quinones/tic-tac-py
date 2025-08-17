print("Loanding...".center(115))
from pygame import mixer
from colorama import Style
import os
import sound

def init_game():
    print(Style.BRIGHT)
    mixer.init()
    sound.music_sound("the_last_of_us.mp3")
    os.system("cls")
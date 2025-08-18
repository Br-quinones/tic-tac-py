#Pantalla completa y zoom
if __name__ == "__main__":
    import keyboard 
    keyboard.press_and_release("alt+enter")

    import time
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)
    
    print("Loanding...".center(115))

    from colorama import Style
    print(Style.BRIGHT)

    import os
    os.system("cls")

    import sound
    sound.innit_sound()
    sound.music_sound("the_last_of_us.mp3")

    import menu
    menu.main_menu()
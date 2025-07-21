#Pantalla completa y zoom
if __name__ == '__main__':
    import keyboard 
    keyboard.press_and_release("f11")

    import time
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)
    
    import sound ; import menu
    
    sound.star_sounds()
    sound.music_sound("the_last_of_us.mp3")
    menu.main_menu()
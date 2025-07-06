#Pantalla completa y zoom
if __name__ == '__main__':
    import keyboard 
    keyboard.press_and_release("f11")

    import time
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)
    
    import menu
    menu.main_menu()









#Pantalla completa y zoom
if __name__ == '__main__':
    import time; import keyboard 
    keyboard.press_and_release("f11")
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)

import tictactoe ; import dialogue
# dialogue.chapter_01()
tictactoe.the_game("expert")







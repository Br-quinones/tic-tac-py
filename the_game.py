import tictactoe; import dialogue #Librerias privadas

current_chapter = "chapter_01"

def chapter_01():
    dialogue.message.role("Te abres paso entre un grupo de estudiantes que vitorean alrededor de una mesa.")
    dialogue.message.role("En el centro, dos chicas se miran fijamente sobre un tablero de tres en raya. Una de ellas sonríe con soberbia.")
    dialogue.message.victoria("¡Jaque mate! O bueno, su equivalente en esto. Nadie puede contra mi lógica.")
    dialogue.message.agatha("Ugh, ¡casi te tenía! Eres demasiado buena, Victoria.")
    dialogue.message.victoria("La práctica hace a la maestra, querida Agatha.")
    dialogue.message.role("Victoria levanta la vista y sus ojos se encuentran con los tuyos.")
    dialogue.message.victoria("Vaya, vaya. ¿Una nueva cara con ganas de un desafío? A ver si tú duras más de un segundo.")
    dialogue.message.agatha("Victoria, no seas así. Quizás solo miraba.")
    dialogue.message.victoria("Tonterías. La mirada de alguien que quiere jugar es inconfundible. ¿Qué dices, te atreves contra la mi?")

    tictactoe.star_round("impossible")

def chapter_02():
    dialogue.message.victoria("Un completo novato que no duro ni un minuto.")
    dialogue.message.victoria("Si quieres la revancha. Derrota antes a mi equipo, puedes empezar con otro principiante.") 
    dialogue.message.agatha("Yo... yo, soy esa principiante tambien.")

    tictactoe.star_round("easy")
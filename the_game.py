import tictactoe; import dialogue #Librerias privadas

current_chapter = "chapter_01"

def chapter_01():
    dialogue.message.role("Entras en una sala bulliciosa, llena de mesas con tableros de tres en raya.")
    dialogue.message.role("En un rincón, una chica te mira y apartando su vista rápidamente.")
    dialogue.message.role("Te acercas y ella se sobresalta un poco.")
    dialogue.message.agatha("H-hola... ¿También vienes a jugar? Yo soy Agatha.")
    dialogue.message.agatha("P-podemos jugar unas partida, pero aunque, recien acabo de conocer este juego.")
    dialogue.message.role("Agatha te ofrece el asiento con una sonrisa nerviosa.")

    tictactoe.star_round("easy")

def chapter_02():
    dialogue.message.agatha("Uh, me has ganastes, veo que ya conoces este juego...")
    dialogue.message.beatrice("Ja, una victoria contra ella no prueba absolutamente nada.")
    dialogue.message.role("Una chica de con gafas te mira con desdén. Es beatrice.")
    dialogue.message.beatrice("Cualquiera puede ganar a esta novata")
    dialogue.message.beatrice("Permíteme darte una lección sobre estrategia real. A ver si así aprendes algo.")

    tictactoe.star_round("medium")

def chapter_03():
    dialogue.message.beatrice("¿Qué? ¡Imposible! Mi estrategia... fue superada")
    dialogue.message.victoria("Vaya vaya es acaso un contricante digno lo que veo.")
    dialogue.message.role("Una chica rubia de mirada desafiante se acerca a la mesa, riéndose a carcajadas.")
    dialogue.message.victoria("Ya me cansé de verte ganar con ese nivel de habilidad tan bajo")
    dialogue.message.victoria("Te voy a enseñar lo que es una verdadera partida mediante la paliza.")

    tictactoe.star_round("hard")

def chapter_04():
    dialogue.message.victoria("Tú... maldita seas... ¡Me ganaste!")
    dialogue.message.role("Victoria golpea la mesa y se va furiosa. Agatha y beatrice te miran con asombro.")
    dialogue.message.director("Vaya, vaya. Has alborotado bastante el gallinero.")
    dialogue.message.role("Un hombre mayor, vestido con un traje rojo, emerge de una oficina.")
    dialogue.message.director("Carne fresca, erase yo el rey indiscutible en esto hasta que un día me acusaron de 'infringir las reglas'.")
    dialogue.message.director("Un participante como tú, con tanto potencial, debe aprender a perder antes que se te suban los humos.")

    tictactoe.star_round("impossible")

def chapter_05():
    dialogue.message.role("Las rondas llegaban y se marchaban, hasta que algo rompio la puerta.")
    dialogue.message.role("Eran unos oficiales, tuvieron que arrestar al director por el bien de la trama")
    dialogue.message.director("Nooo maldito guión ¡Yo volvere y encontraré la forma de aplastarte!")
    dialogue.message.agatha("¿¡Oye eso es trampa!?")
    dialogue.message.beatrice("¿Acaban de arrestar al director por una partida del 3 en raya?")
    dialogue.message.victoria("Y ademas que mierda con esa voz que habla todo en tercera persona ¡nada tiene sentido!")
    dialogue.message.role("Con la derrota del director y de todos tus contrincantes ¡obtuviste la victoria absoluta!")
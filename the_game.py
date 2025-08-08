import tictactoe; import dialogue #Librerias privadas

current_chapter = "chapter_01"

def chapter_01():
    dialogue.message.role("Entras en una sala bulliciosa, llena de mesas con tableros de tres en raya.")
    dialogue.message.role("En un rincón, una chica te mira y apartando su vista rápidamente.")
    dialogue.message.role("Te acercas y ella se sobresalta un poco.")
    dialogue.message.agatha("H-hola... ¿También vienes a jugar? Yo soy Agatha.")
    dialogue.message.agatha("P-podemos jugar unas partida, asi aprendemos las reglas de este juego juntos.")
    dialogue.message.role("Agatha te ofrece el asiento con una sonrisa nerviosa.")

    tictactoe.star_round("easy")

def chapter_01_lose():
    dialogue.message.agatha("¡Oh! H-he ganado. ¡No me lo puedo creer!")
    dialogue.message.agatha("Ha sido una partida muy divertida. Vamos por la revancha.")

def chapter_02():
    dialogue.message.agatha("Uh, me has ganastes, veo que ya conoces este juego...")
    dialogue.message.beatrice("Ja, una victoria contra ella no prueba absolutamente nada.")
    dialogue.message.role("Una chica, de pelo largo, te mira con desdén. Es beatrice.")
    dialogue.message.beatrice("Cualquiera puede ganar a esta novata")
    dialogue.message.beatrice("Permíteme darte una lección sobre estrategia real. A ver si así aprendes algo.")

    tictactoe.star_round("medium")
    
def chapter_02_lose():
    dialogue.message.beatrice("Ja, tan facil, como quitarle un caramelo a un niño.")
    dialogue.message.beatrice("Consedeme el placer de volverte a ganar en un nuevo round.")

def chapter_03():
    dialogue.message.beatrice("¿Qué? ¡Imposible! Mi estrategia... fue superada.")
    dialogue.message.victoria("Vaya vaya es acaso un contricante digno lo que veo.")
    dialogue.message.role("Una chica con flequillo asimetrico de mirada desafiante se acerca a la mesa, riéndose a carcajadas.")
    dialogue.message.victoria("Ya me cansé de verte ganar con ese nivel de habilidad tan bajo")
    dialogue.message.victoria("Te voy a enseñar lo que es una verdadera partida mediante la paliza.")

    tictactoe.star_round("hard")

def chapter_03_lose():
    dialogue.message.victoria("JAJAJAJA; JAJAJAJA, sin duda la partida más facil de mi existencia.")
    dialogue.message.victoria("Te ves molesto. Acaso quieres recuper tu dignitad, ¡INTENTALO...!")

def chapter_04():
    dialogue.message.victoria("Tú... maldita seas... ¡Me ganaste!")
    dialogue.message.role("Victoria golpea la mesa y se va furiosa. Agatha y beatrice te miran con asombro.")
    dialogue.message.director("¡Carajo! ¿Qué está pasando aquí? ¿A qué se debe tanta algarabía?")
    dialogue.message.role("Un hombre mayor, vestido con un traje rojo, emerge de una oficina.")
    dialogue.message.director("Heh erase yo el rey indiscutible en esto hasta que un día me acusaron de 'infringir las reglas'.")
    dialogue.message.director("Un participante como tú, con tanto potencial, debe aprender a perder antes que se te suban los humos.")

    tictactoe.star_round("impossible")

def chapter_04_lose():
    dialogue.message.director("No te frustes, ni te enojes, puesto que la victoria siempre recaera en mi.")
    dialogue.message.director("Pero ahora estas atrapado en mi conquista del triunfo constantes.")

def chapter_05():
    dialogue.message.role("Las rondas llegaban y se marchaban, hasta que algo rompio la puerta.")
    dialogue.message.role("Era la policia, tuvieron que arrestar al director por el bien de la trama")
    dialogue.message.director("¿Que? Noooo maldito guión ¡Volvere, volvere y te muy fuerte de aplastare!")
    dialogue.message.agatha("¿¡Que eso es legal!?")
    dialogue.message.beatrice("¿Acaso... acaban de arrestar al director por una partida del 3 en raya?")
    dialogue.message.beatrice("¡Nada tiene sentido en este lugar!")
    dialogue.message.victoria("¡Y además, qué demonios con esa voz que habla todo en tercera persona! ¡Nada tiene sentido!")
    dialogue.message.role("Con la derrota del director y de todos tus contrincantes ¡obtuviste la victoria absoluta!")
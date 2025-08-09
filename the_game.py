import tictactoe; import dialogue #Librerias privadas

current_chapter = "chapter_01"

class chapter_01():
    def history():
        dialogue.message.role("Entras en una sala bulliciosa, repleta de mesas con tableros de tres en raya.")
        dialogue.message.role("En un rincón, una chica te observa y aparta la vista con timidez.")
        dialogue.message.role("Te acercas y ella se sobresalta un poco.")
        dialogue.message.agatha("—H-hola... ¿También vienes a jugar? Yo soy Agatha.")
        dialogue.message.agatha("Puedo enseñarte las reglas si quieres. Así practicamos.")
        dialogue.message.role("Agatha te ofrece el asiento con una sonrisa nerviosa.")

        tictactoe.star_round("medium")
        
    def player_lose_01():
        dialogue.message.agatha("¡Oh! H-he ganado... No me lo esperaba.")
        dialogue.message.agatha("Ha sido una partida entretenida.")

    def player_win_01():
        dialogue.message.agatha("Vaya... me has ganado. Veo que ya tienes experiencia en esto.")
        dialogue.message.agatha("Bueno, igual gracias por jugar conmigo.")

    def player_draw_01():
        dialogue.message.agatha("Vaya Empate... Fue una partida algo sosa.")
        dialogue.message.agatha("Vamos por otra para desempatar.")


class chapter_02():
    def history():
        dialogue.message.beatrice("Ja. Una victoria contra una novata no demuestra nada.")
        dialogue.message.role("Una chica de pelo largo y gesto altivo te observa con desdén. Es Beatrice.")
        dialogue.message.beatrice("Cualquiera puede vencer a la gente que ni conoce las reglas del juego.")
        dialogue.message.beatrice("Déjame mostrarte lo que puedo hacer yo. Tal vez aprendas algo útil.")

        tictactoe.star_round("hard")

    def player_lose_02():
        dialogue.message.beatrice("Ja, tan fácil como quitar un caramelo a un niño.")
        dialogue.message.beatrice("Vamos, concédeme el gusto de derrotarte otra vez.")

    def player_win_02():
        dialogue.message.beatrice("¿Qué? ¡Imposible! Mi estrategia ha sido superada.")
        dialogue.message.beatrice("¡Como es que lograstes pulverizar mi defensa!")

    def player_draw_02():
        dialogue.message.beatrice("Hmph. Un empate. No me satisface.")
        dialogue.message.beatrice("Perfeccionare mí tactica para un round más.")


class chapter_03():
    def history():
        dialogue.message.victoria("Vaya, vaya... parece que hay un rival interesante aquí.")
        dialogue.message.role("Una chica con flequillo asimétrico y mirada desafiante se acerca riéndose en voz baja.")
        dialogue.message.victoria("Me canse de ver partidas mediocres. Te daré una lección que recordarás.")
        dialogue.message.victoria("Prepárate que en mi no existe piedad, solo habilidad.")

        tictactoe.star_round("expert")

    def player_lose_03():
        dialogue.message.victoria("¡JAJA! Sin duda, la victoria más sencilla de mi vida.")
        dialogue.message.victoria("¿Quieres recuperar tu orgullo? Ven e inténtalo de nuevo...")

    def player_win_03():
        dialogue.message.victoria("Tú... maldita seas... ¡me ganaste!")
        dialogue.message.victoria("Tan solo es tu... tu... agh.")

    def player_draw_03():
        dialogue.message.victoria("¡Empate! Esto ha sido... inesperado.")
        dialogue.message.victoria("Pero no te confies que la victoria es siempre mía.")

        
class chapter_04():
    def history():
        dialogue.message.director("¿Qué está pasando aquí? A qué se debe esta algarabía.")
        dialogue.message.role("Un hombre mayor, vestido con un traje rojo, emerge de una oficina. Es el Director.")
        dialogue.message.director("Antes fui el rey de estas partidas... hasta que me acusaron de 'infringir las reglas'.")
        dialogue.message.director("Un participante con tanto potencial como tú debe aprender que es la derrota.")
        dialogue.message.role("El Director te mira con una sonrisa fría; sus ojos brillan con imposición y reto.")

        tictactoe.star_round("impossible")

    def player_lose_04():
        dialogue.message.director("No te frustres. La victoria siempre recaerá en mí.")
        dialogue.message.director("Yo estoy para enseñarte lo que es perder.")

    def player_win_04():
        dialogue.message.director("...¿Cómo es posible? ¿Me has vencido?")
        dialogue.message.director("Interesante. Tendré que revisar mis 'métodos'. Esto no ha terminado.")

    def player_draw_04():
        dialogue.message.director("Empate. Eso sera a lo maximo que puedes aspirar.")
        dialogue.message.director("Vamos por unas más hasta que logre mi victoria.")


class chapter_05():
    def history():
        dialogue.message.role("Las rondas pasaban y la luz del atardecer aparecia... hasta que la puerta se abrió un golpe.")
        dialogue.message.role("La policía irrumpió y se llevó al Director por delitos contra el guión.")
        dialogue.message.director("¿Qué? ¡Nooooo! Maldito guión... ¡Yo volveré y aplastaré a todos!")
        dialogue.message.agatha("¿¡Que acaso eso es legal!?")
        dialogue.message.beatrice("¿De verdad acaban de arrestar al Director por unas partidas del 3 en raya?")
        dialogue.message.victoria("¡Nada tiene sentido en este lugar! Además, que demonios con esa voz que habla en tercera persona.")
        dialogue.message.role("Con la caída del Director, obtienes la victoria en la sala.")

        print("xd")

import tictactoe
import dialogue
import menu  # Librerías privadas

current_chapter = "chapter_01"

class chapter_01():
    def history():
        dialogue.message.role("Entras en una sala bulliciosa, repleta de mesas con tableros de tres en raya.")
        dialogue.message.role("En un rincón, una chica te observa y aparta la vista con timidez.")
        dialogue.message.role("Te acercas y ella se sobresalta un poco.")
        dialogue.message.agatha("—H-hola... ¿También vienes a jugar? Yo soy Agatha.")
        dialogue.message.agatha("Puedo enseñarte las reglas si quieres. Así practicamos.")
        dialogue.message.role("Agatha te ofrece un asiento con una sonrisa nerviosa.")

        tictactoe.star_round("easy")
        
    def player_lose_01():
        dialogue.message.agatha("¡Oh! H-he ganado... No me lo esperaba.")
        dialogue.message.agatha("Esta ha sido una partida entretenida.")

    def player_win_01():
        dialogue.message.agatha("Vaya... me has ganado. Veo que ya tienes experiencia en este juego.")
        dialogue.message.agatha("Bueno, igual gracias por jugar conmigo.")

    def player_draw_01():
        dialogue.message.agatha("Vaya empate... Fue una partida algo sosa.")
        dialogue.message.agatha("Vamos por otra para desempatar.")


class chapter_02():
    def history():
        dialogue.message.beatrice("Ja. Una victoria contra una novata no demuestra nada.")
        dialogue.message.role("Una chica de pelo largo y gesto altivo te observa con desdén. Es Beatrice.")
        dialogue.message.beatrice("Cualquiera puede vencer a la gente que no conoce ni las reglas.")
        dialogue.message.beatrice("Déjame mostrarte lo que puedo hacer yo. Tal vez aprendas algo útil.")

        tictactoe.star_round("medium")

    def player_lose_02():
        dialogue.message.beatrice("Ja, tan fácil como quitar un caramelo a un niño.")
        dialogue.message.beatrice("Vamos, concédeme el gusto de derrotarte otra vez.")

    def player_win_02():
        dialogue.message.beatrice("¿Qué? ¡Imposible! Mi estrategia ha sido superada.")
        dialogue.message.beatrice("¡¿Cómo lograste superar mi defensa?!")

    def player_draw_02():
        dialogue.message.beatrice("Hmph. Un empate. No me satisface.")
        dialogue.message.beatrice("Perfeccionaré mi defensa para un round más.")


class chapter_03():
    def history():
        dialogue.message.victoria("Vaya, vaya... parece que hay un digno rival aquí.")
        dialogue.message.role("Una chica con flequillo asimétrico y mirada desafiante se acerca riéndose en voz baja.")
        dialogue.message.victoria("Me canso de ver partidas tan mediocres. Yo te daré una lección inolvidable.")
        dialogue.message.victoria("Prepárate, porque en mí no existe piedad, solo habilidad.")

        tictactoe.star_round("hard")

    def player_lose_03():
        dialogue.message.victoria("¡JAJA! Sin duda, la victoria más sencilla de toda mi vida.")
        dialogue.message.victoria("¿Quieres recuperar tu orgullo? Pues ven e inténtalo de nuevo...")

    def player_win_03():
        dialogue.message.victoria("Tú... maldita sea... ¡me ganaste!")
        dialogue.message.victoria("Tan solo es tu... tu... agh.")

    def player_draw_03():
        dialogue.message.victoria("¡Empate! Esto ha sido... inesperado.")
        dialogue.message.victoria("Pero ni te confíes, la victoria siempre será mía.")


class chapter_04():
    def history():
        dialogue.message.director("¿Qué está pasando aquí? ¿A qué se debe tanto ruido?")
        dialogue.message.role("Un hombre mayor, vestido con un traje rojo, emerge de una oficina.")
        dialogue.message.director("Ahhh, unas partidas de tres en raya.")
        dialogue.message.director("Antes era el rey de este juego... hasta que tuve que retirarme para ser director.")
        dialogue.message.director("Un participante con tanto potencial como tú debe aprender lo que es la derrota.")
        dialogue.message.role("El Director te mira con una sonrisa fría; sus ojos brillan con desafío y reto.")

        tictactoe.star_round("expert")

    def player_lose_04():
        dialogue.message.director("No te frustres. La victoria siempre será mía.")
        dialogue.message.director("Yo existo para enseñarte lo que es perder.")

    def player_win_04():
        dialogue.message.director("...¿Cómo es posible? ¿Me has vencido?")
        dialogue.message.director("Impresionante, eres toda una máquina en esto.")

    def player_draw_04():
        dialogue.message.director("Uhhh, empate. Bueno, eso será lo máximo a lo que puedes aspirar.")
        dialogue.message.director("Vamos por unas más, hasta que logre mi victoria. Tu única salida.")


class chapter_05():
    def history():
        dialogue.message.role("...............................................................................................")
        dialogue.message.agatha("Felicidades...")
        dialogue.message.beatrice("Felicidades...")
        dialogue.message.victoria("Felicidades...")
        dialogue.message.director("Felicidades...")
        dialogue.message.role("Felicidades, jugador. Has alcanzado la victoria absoluta...")
        dialogue.message.role("The End.")

        menu.main_menu()


class event():
    ########## Humillaciones al perder ##########
    def humiliation_agatha():
        dialogue.message.agatha("Claro que sí, sigamos practicando. Una revancha estaría genial.")

    def humiliation_beatrice():
        dialogue.message.beatrice("Oh sí, ya me veo ganándote otra vez. Te daré la revancha solo para vencerte una vez más.")

    def humiliation_victoria():
        dialogue.message.victoria("¿En serio crees que tienes oportunidad de ganarme en una revancha? Te demostraré que no.")

    def humiliation_director():
        dialogue.message.director("¿Revancha? Pide cuantas quieras, el resultado será siempre el mismo.")

    ########## Ayuda al perder ##########
    def help_agatha():
        dialogue.message.agatha("JAJAJAJAJAJAJAJA...")
        dialogue.message.role("Solo usa los conocimientos básicos del tres en raya. Utiliza el teclado como control.")

    def help_beatrice():
        dialogue.message.beatrice("JAJAJAJAJAJAJAJA...")
        dialogue.message.role("Beatrice solo sabe defenderse, nunca atacará. Utiliza eso en su contra.")

    def help_victoria():
        dialogue.message.victoria("JAJAJAJAJAJAJAJA...")
        dialogue.message.role("Victoria sabe atacar y defenderse. Piensa en algo diferente.")

    def help_director():
        dialogue.message.director("JAJAJAJAJAJAJAJA...")
        dialogue.message.role("Si quieres ganar, copia la jugada del menú... y tu cuarta jugada en la esquina.")

    ########## Rendición total ##########
    def surrender():
        dialogue.message.role("Sientes tanta humillación que decides escapar de la habitación.")
        dialogue.message.role("No volteas la mirada al escapar, pero sientes la suave risa del enemigo.")

    ########## Error ##########
    def chapter_error():
        dialogue.message.role("Ehhh... si estás viendo esto es que el desarrollador cometió un error jajaja.")
        dialogue.message.role("Te mandaré al menú y de ahí reiniciaremos la partida.")
        menu.main_menu()

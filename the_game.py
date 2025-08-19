import tictactoe; import dialogue; import menu; import traductor # Librerías privadas

current_chapter = "chapter_01"

class chapter_01():

    def history():
        l = traductor.traductor_of_the_game()
        # dialogue.message.role(l.chapter_01_history_message_01)
        # dialogue.message.role(l.chapter_01_history_message_02)
        # dialogue.message.role(l.chapter_01_history_message_03)
        # dialogue.message.agatha(l.chapter_01_history_agatha_01)
        # dialogue.message.agatha(l.chapter_01_history_agatha_02)
        # dialogue.message.role(l.chapter_01_history_message_04)

        tictactoe.star_round("hard")
        
    def player_lose_01():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.chapter_01_player_lose_01_agatha_01)
        dialogue.message.agatha(l.chapter_01_player_lose_01_agatha_02)

    def player_win_01():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.chapter_01_player_win_01_agatha_01)
        dialogue.message.agatha(l.chapter_01_player_win_01_agatha_02)

    def player_draw_01():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.chapter_01_player_draw_01_agatha_01)
        dialogue.message.agatha(l.chapter_01_player_draw_01_agatha_02)


class chapter_02():
    def history():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.chapter_02_history_beatrice_01)
        dialogue.message.role(l.chapter_02_history_message_01)
        dialogue.message.beatrice(l.chapter_02_history_beatrice_02)
        dialogue.message.beatrice(l.chapter_02_history_beatrice_03)

        tictactoe.star_round("medium")

    def player_lose_02():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.chapter_02_player_lose_02_beatrice_01)
        dialogue.message.beatrice(l.chapter_02_player_lose_02_beatrice_02)

    def player_win_02():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.chapter_02_player_win_02_beatrice_01)
        dialogue.message.beatrice(l.chapter_02_player_win_02_beatrice_02)

    def player_draw_02():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.chapter_02_player_draw_02_beatrice_01)
        dialogue.message.beatrice(l.chapter_02_player_draw_02_beatrice_02)


class chapter_03():
    def history():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.chapter_03_history_victoria_01)
        dialogue.message.role(l.chapter_03_history_message_01)
        dialogue.message.victoria(l.chapter_03_history_victoria_02)
        dialogue.message.victoria(l.chapter_03_history_victoria_03)

        tictactoe.star_round("hard")

    def player_lose_03():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.chapter_03_player_lose_03_victoria_01)
        dialogue.message.victoria(l.chapter_03_player_lose_03_victoria_02)

    def player_win_03():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.chapter_03_player_win_03_victoria_01)
        dialogue.message.victoria(l.chapter_03_player_win_03_victoria_02)

    def player_draw_03():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.chapter_03_player_draw_03_victoria_01)
        dialogue.message.victoria(l.chapter_03_player_draw_03_victoria_02)


class chapter_04():
    def history():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.chapter_04_history_director_01)
        dialogue.message.role(l.chapter_04_history_message_01)
        dialogue.message.director(l.chapter_04_history_director_02)
        dialogue.message.director(l.chapter_04_history_director_03)
        dialogue.message.director(l.chapter_04_history_director_04)
        dialogue.message.role(l.chapter_04_history_message_02)

        tictactoe.star_round("expert")

    def player_lose_04():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.chapter_04_player_lose_04_director_01)
        dialogue.message.director(l.chapter_04_player_lose_04_director_02)

    def player_win_04():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.chapter_04_player_win_04_director_01)
        dialogue.message.role(l.chapter_04_player_win_04_message_01)

    def player_draw_04():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.chapter_04_player_draw_04_director_01)
        dialogue.message.director(l.chapter_04_player_draw_04_director_02)


class chapter_05():
    def history():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.chapter_05_history_agatha_01)
        dialogue.message.beatrice(l.chapter_05_history_beatrice_01)
        dialogue.message.victoria(l.chapter_05_history_victoria_01)
        dialogue.message.director(l.chapter_05_history_director_01)
        dialogue.message.role(l.chapter_05_history_message_01)

        menu.main_menu()


class event():
    ########## Humillaciones al perder ##########
    def humiliation_agatha():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.event_humiliation_agatha_01)

    def humiliation_beatrice():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.event_humiliation_beatrice_01)

    def humiliation_victoria():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.event_humiliation_victoria_01)

    def humiliation_director():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.event_humiliation_director_01)

    ########## Ayuda al perder ##########
    def help_agatha():
        l = traductor.traductor_of_the_game()
        dialogue.message.agatha(l.event_help_agatha_01)
        dialogue.message.role(l.event_help_agatha_02)

    def help_beatrice():
        l = traductor.traductor_of_the_game()
        dialogue.message.beatrice(l.event_help_beatrice_01)
        dialogue.message.role(l.event_help_beatrice_02)

    def help_victoria():
        l = traductor.traductor_of_the_game()
        dialogue.message.victoria(l.event_help_victoria_01)
        dialogue.message.role(l.event_help_victoria_02)

    def help_director():
        l = traductor.traductor_of_the_game()
        dialogue.message.director(l.event_help_director_01)
        dialogue.message.role(l.event_help_director_02)

    ########## Rendición ##########
    def surrender():
        l = traductor.traductor_of_the_game()
        dialogue.message.role(l.event_surrender_message_01)
        dialogue.message.role(l.event_surrender_message_02)

    ########## Error ##########
    def chapter_error():
        l = traductor.traductor_of_the_game()
        dialogue.message.role(l.event_chapter_error_message_01)
        dialogue.message.role(l.event_chapter_error_message_02)
        menu.main_menu()
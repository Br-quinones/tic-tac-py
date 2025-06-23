#                                              Tic-Tac-Py
#
# Una novela visual sobre el un enfrentaminto de varios jovenes en el 3 en raya. 
#
#Pilares
    #1. Segir aprendiendo python
    #2. Giros en la jugabilidad del 3 en raya.
    #3. Una buena historia (Cueste lo que cueste).
    #4. Usar arte Ascci para Todo.
    #5. El juego deve durar menos de 10 minutos.
    #6. Aprender a usar json para soporte de idiomas
#
#Historia 
    #Estas en un instituto, pasando logras observas que dos chicas se enfrentan en el 3 en raya de manera intensa. Te acercas y ahora es cuando te reta a ti. Las primeras partidas seran las tipicas partidas pero mientras se avance las la jugabilidad cambiara, ejemplo si antes eran 3 en raya ahora en esta ronda sera del 4 en raya. Una vez que ganes o pierdas obtendras el final bueno o malo.
#
#Personajes
    #Roleo --> Cian
        #Este no es un persnaje, pero se utilizara para representar acciones en tercera persona osea el narrador.
    #Jugador --> Azul
        #Solo es el nombre base de cada jugador, que el jugador podra cambiar cuando la historia le requiera.
    #Agatha --> Verde
        #Jugadora de bajo nivel que te introducera en el juego con personalidad: timida y reservada.
    #Beatriz --> Magenta
        #Jugadora con nivel medio que introducera nuevas mecanicas al 3 en raya con personalidad: intelectual y elitista.
    #Victoria --> Amarillo
        #Jugadora de alto nivel que te dara un duro desafio con personalidad: agresiva, burlona y grosera.
    #Director --> Rojo
        #Ex-jugador retirado por infracciones en las reglas que vuelve para darte una paliza personalidad: tramposo y malvado.
#
#Jugabilidad
#Solo me centrare en las variaciones del 3 en raya.
    #1. El clasico 3 en raya. No hay variacion en nada.
    #2. Convertir los X y O en ▢. El objetivo es obligar al jugador recordar cuales son y no son sus fichas.
    #3. Pasar del 3 en raya al 1 en raya. El objetivo es una partida injusta.
    #4. Pasar del 3 en raya al 2 en raya. El objetivo es una partida injusta.
    #5. Pasar del 3 en raya al 4 en raya. El objetivo es una partida mas dificil.
    #6. Limite de fichas. Solo tienes 3 fichas y si colocas una 4° la primera se mueve a ese lugar.
    #7. Limite de tiempo. Tienes solo unos segundos para pensar y jugar.
    #8. Aletorio comienzo. Una ficha tuya y del enemigo son colocadas aletoriamente al comenzar la partida.
    #9. El que gana pierde. Una version donde evitaras ganar.
    #10. Una ficha ya puesta del enemigo. Empezar con ventaja el enemigo eso nomas.
#
#Progresión
    #Ganar
        #Capitulo 1: Al acercarte a una batalla del 3 en raya eres retado, inicias jugando con una aprendiz.
        #Capitulo 2: Luego te enfrentaras a una persona mas experimetada, ahora implemetando nuevas variantes del 3 en raya.
        #Capitulo 3: Ganandole ahora tendras que ir por la jefa de grupo con batallas agresivas y mas desafiantes
        #Capitulo 4: Si logras ganar tendras una batalla con el director cual jugara de manera injusta y tramposa
    #Perder 
        #Solo se reinicia la partida hasta ganar. Pero al reinicar de burlan y humillaran como penalización.
#
#Scope
    #Partidas: 4 para cada personaje enemigo se le asigna una ronda(cada ronda con 3 victorias para elegir ganador)
    #Duración: Menos de 10 minutos si o si para todo el juego.
# 
#Produccion y requisitos
    #Produccion: Lo hare todo yo y correciones ortotipograficas lo hara la AI.
    #Requisitos: 0 centavos y unos 4 meses para acabarlo. Se añaden 3 meses por motivos de estudio.
# 
#Herramientas
    #VSC: Editor de texto.
    #Python: El lenguaje de programacion.
    #Json: Para soporte de idiomas
    #Kapwing: Para editar musica.
    #GitHub: Para control de versiones.
# 
#Audiecia
    #Para la pagina itch.io
    #Puede ser algunos conocidos
# 
#Costo
    #Totalmente gratis y codigo publico.
#
#Interfaces
#Deve de predominar el color rojo en todas las interfaces.
    #Dialogos
        #######################################
        #      Arte Ascci del personaje:      #
        #               ###                   #
        #           #    #    #               #
        #            # # # ##                 #
        #                #                    #
        #######################################
        #     Name: Texto que pronuncia.      #
        #                                     #
        #######################################
    #Menu
        #######################################
        #            Tic-Tac-Py               #
        #                                     #
        #[1]Play [2]Setting [3]Credits [4]Exit#
        #                                     #
        #      #        |X| |O|        #      #
        #      #  #     |O|X|O|     #  #      #
        #    # # #      | |O|X|      # # #    #
        #   #                             #   #
        #######################################
    #3 en raya
        #######################################
        #              3  -  4                #
        #              |O|X|O|                #
        #              | |O|X|                #
        #              |X| |O|                #
        #######################################                                    
        #                 ↑                   #
        #              ←  ↓  →                #
        #                                     #
        #######################################
#
#Autor
    #Br-Quiñones


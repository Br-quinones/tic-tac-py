from pygame import mixer 

#Channel_0: Musica de fondo // .mp3
#Channel_1: Efectos de sonido // .wav
#Channel_2: Bucles de sonido // .ogg

def star_sounds():
    mixer.init()

def music_sound(music):
    mixer.Channel(0).play(mixer.Sound(f"audio/musics/{music}"), 0)

def effect_sound(effect):
    mixer.Channel(1).play(mixer.Sound(f"audio/effects/{effect}"), 0)

def loop_sound(loop):
    mixer.Channel(2).play(mixer.Sound(f"audio/loops/{loop}"), -1)
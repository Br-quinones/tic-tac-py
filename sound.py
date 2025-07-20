from pygame import mixer 

mixer.init()

def star_sound_loop(bleep):
    mixer.music.load(f"audio/loops/{bleep}.ogg")
    mixer.music.play(-1)

def star_sound_efect(efect):
    mixer.music.load(f"audio/{efect}")
    mixer.music.play()

def star_sound_efect_channel():
    mixer.Channel(1).play(mixer.Sound("audio/move.mp3"))
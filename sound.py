from pygame import mixer 

def star_sound():
    mixer.init()

def star_sound_loop(bleep):
    mixer.music.load(f"audio/loops/{bleep}.ogg")
    mixer.music.play(-1)

def star_sound_efect(efect):
    mixer.music.load(f"audio/{efect}.ogg")
    mixer.music.play()
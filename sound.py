from pygame import mixer 

mixer.init()

def star_sound_loop(bleep):
    mixer.music.load(f"audio/loops/{bleep}.ogg")
    mixer.music.play(-1)

def star_sound_efect(file_the_of_audio):
    mixer.music.load(file_the_of_audio)
    mixer.music.play()

def star_sound_efect_channel(file_the_of_audio):
    mixer.Channel(1).play(mixer.Sound(file_the_of_audio))
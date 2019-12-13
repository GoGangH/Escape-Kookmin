from settings import *
from os import path
import pygame as pg
def set_music(filename):
    bgm_folder = path.join(GAME_DIR, 'bgm')
    pg.mixer.music.load(path.join(bgm_folder, filename))
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play(-1)

def set_sfx(filename):
    sfx_folder = path.join(GAME_DIR, 'sfx')
    effect = pg.mixer.Sound(path.join(sfx_folder, filename))
    effect.play()

from settings import *
from os import path
import pygame as pg
def set_music(filename):
    #bgm 설정
    bgm_folder = path.join(game_dir, 'bgm')
    pg.mixer.music.load(path.join(bgm_folder, filename))
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play(-1)

def set_sfx(filename):
    #효과음 설정
    sfx_folder = path.join(game_dir, 'sfx')
    effect = pg.mixer.Sound(path.join(sfx_folder, filename))
    effect.play()

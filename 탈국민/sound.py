from settings import *
from os import path
import pygame as pg
def set_music(filename, volume=0.5):
    '''bgm을 설정. 인자는 파일명'''
    bgm_folder = path.join(GAME_DIR, 'bgm')
    pg.mixer.music.load(path.join(bgm_folder, filename))
    pg.mixer.music.set_volume(volume)
    pg.mixer.music.play(-1)

def set_sfx(filename, volume=0.5):
    '''효과음을 설정. 인자는 파일명, 볼륨'''
    sfx_folder = path.join(GAME_DIR, 'sfx')
    effect = pg.mixer.Sound(path.join(sfx_folder, filename))
    effect.set_volume(volume)
    effect.play()
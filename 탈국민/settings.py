'''
게임의 상수값 설정
'''
import os
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 960
HEIGHT =  540
FPS = 60
TITLE = "탈 국민"
BGCOLOR = DARKGREY

TILESIZE = 48
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#map setting
STAGELEVEL = 0
STAGETMX = ['showerRoom.tmx', 'fitness.tmx', 'secondfloor.tmx', '4thfloor.tmx']
STAGENAME = ['shower', 'fitness', 'secondfloor', '4thfloor']
PORTALMAP = {
    'fitness' : 1,
    'shower' : 0,
    'secondfloor' : 2,
}

#tutorial setting
STARTIMAGE = 'start.png'
TUTORIALIMAGE = ['p0.png', 'p1.png', 'p2.png', 'p3.png']
PAGEBLACK = 'black2.png'

#player settings
PLAYER_SPEED = 180
PLAYER_IMG = 'player.png'
PLAYERCHANGE_IMG = 'player2.png'

#Light Shadowing
SHADOW_COLOR = (20, 20, 20)
LIGHTMASK = 'light.png'
LIGHT_RADIUS = (300, 300)

#chat settings
CHAT_WIDTH = WIDTH/2
CHAT_HEIGHT = 20
CHAT_IMG = 'chat.png'

#sound setting
SOUNDLIST = ['backgrund.mp3','19.ogg','14.ogg', 'prologue.mp3', 'break.wav']
game_dir = os.path.dirname(__file__)
BGM = os.listdir(os.path.join(game_dir, 'bgm'))
SFX = os.listdir(os.path.join(game_dir, 'sfx'))

import pygame as pg
from settings import *
import time
from chat import *
from sound import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, screen, stage):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'image')
        self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMG)).convert_alpha()
        self.beforKey = None
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.Beforpos = self.pos
        self.screen = screen
        self.chat = None
        self.chating = False
        self.Mapstage = stage
        self.stupidDegree = 0
        self.stageChk = {
            'cloth' : 0,
            'clothPortal' : 0,
            'muscle' : 0,
        }
        self.stageDialogue = {
            'start' : 0,
        }

    def set_pos(self, x, y):
        self.pos = vec(x, y)
        
    def get_keys(self):
        self.vel = vec(0, 0)
        self.keys = pg.key.get_pressed()

        if self.chating == False:
            if self.keys[pg.K_LEFT] or self.keys[pg.K_a]:
                self.vel.x = -PLAYER_SPEED
                #if(keys!=self.beforKey):
                    #self.image = pg.transform.flip(self.image, False, True)
            elif self.keys[pg.K_RIGHT] or self.keys[pg.K_d]:
                self.vel.x = PLAYER_SPEED
                #if(keys!=self.beforKey):
                    #self.image = pg.transform.flip(self.image, False, True)
            elif self.keys[pg.K_UP] or self.keys[pg.K_w]:
                self.vel.y = -PLAYER_SPEED
            elif self.keys[pg.K_DOWN] or self.keys[pg.K_s]:
                self.vel.y = PLAYER_SPEED
            elif self.keys[pg.K_SPACE]:
                self.chk_items()
                time.sleep(0.5)
            if self.vel.x != 0 and self.vel.y != 0:
                self.vel *= 0.7071
        else:
            if self.keys[pg.K_f]:
                self.chating = False
            if self.keys[pg.K_SPACE]:
                '''time.sleep 걸고 쓰면 space로 페이지 넘기기 가능'''
                if self.chat.hasNextPage():
                    self.chat.drawchat()
                    time.sleep(0.5)
                else:
                    self.chating = False
                    time.sleep(0.2)

        self.beforKey = self.keys

    def chk_walls(self, dir):
    #캐릭터를 움직이기 전에 벽이 있는지 확인
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
    
    def chk_items(self):
        hits = pg.sprite.spritecollide(self, self.game.items, False)
        if hits:
            set_sfx(SOUNDLIST[1])
            for sprite in hits:
                if sprite.name == 'cloth' :
                    self.chating = True
                    self.chat = Chat(self.screen, sprite.dialoguelist, self.stageChk['cloth'])
                    self.chat.drawchat()
                    self.stageChk[sprite.name] = 1
                    self.image = pg.image.load(os.path.join(self.img_folder, PLAYERCHANGE_IMG)).convert_alpha()
                if sprite.name == 'strong' :
                    self.chating = True
                    self.chat = Chat(self.screen, sprite.dialoguelist, 0)
                    self.chat.drawchat()
                    self.stageChk['muscle'] = 1
                else :
                    self.chating = True
                    self.chat = Chat(self.screen, sprite.dialoguelist, 0)
                    self.chat.drawchat()
        else:
            chatting = [['멍청하게 시간을 날리고 있다.'],['걷는건 space가 아니라 w키다'],['bug인가?'],['그만해 이제 대사없어']]
            self.chating = True
            self.chat = Chat(self.screen, chatting, self.stupidDegree)
            self.chat.drawchat()
            self.stupidDegree+=1
            self.stupidDegree%=len(chatting)

    def chk_potal(self):
        hits = pg.sprite.spritecollide(self, self.game.portals, False)
        if hits and self.chating == False:
            for sprite in hits:
                if sprite.name == 'fitness' :
                    if self.stageChk['cloth'] == 0:
                        self.pos = self.Beforpos
                        self.pos.y-=20
                        self.chat = Chat(self.screen, sprite.dialoguelist, self.stageChk['clothPortal'])
                        self.chat.drawchat()
                        self.chating = True
                        time.sleep(0.2)
                        if self.stageChk['clothPortal']==0:
                            self.stageChk['clothPortal']=1
                    else:
                        set_sfx(SOUNDLIST[2])
                        self.Mapstage=PORTALMAP[sprite.name]
                elif sprite.name == 'secondfloor' :
                    if self.stageChk['muscle'] == 0:
                        self.pos = self.Beforpos
                        self.pos.x+=20
                        self.chat = Chat(self.screen, sprite.dialoguelist, 0)
                        self.chat.drawchat()
                        self.chating = True
                        time.sleep(0.2)
                    elif self.stageChk['muscle'] == 1:
                        set_sfx(SOUNDLIST[4])
                        self.chat = Chat(self.screen, sprite.dialoguelist, 1)
                        self.chat.drawchat()
                        self.chating = True
                        time.sleep(1)
                        self.Mapstage=PORTALMAP[sprite.name]
                        self.stageChk['muscle']=2
                    else :
                        set_sfx(SOUNDLIST[2])
                        self.Mapstage=PORTALMAP[sprite.name]
                else:
                    set_sfx(SOUNDLIST[2])
                    self.Mapstage=PORTALMAP[sprite.name]
        else:
            self.Beforpos = self.pos
    
    def chkdialogue(self):
        hits = pg.sprite.spritecollide(self, self.game.dialogues, False)
        if hits:
            for sprite in hits:
                if self.stageDialogue[sprite.name] == 0:
                    self.chat = Chat(self.screen, sprite.dialoguelist, self.stageChk['clothPortal'], '쿠민')
                    self.chat.drawchat()
                    self.chating = True
                    time.sleep(0.2)
                    self.stageDialogue[sprite.name]=1

    def update(self):
    #캐릭터 위치 업데이트
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.chk_walls('x')
        self.rect.y = self.pos.y
        self.chk_walls('y')
        self.chk_potal()
        self.chkdialogue()

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Item(pg.sprite.Sprite):
    def __init__(self, game, type, x, y, w, h, properties):
        self.name = type
        self.groups = game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.properties = properties
        self.dialoguelist = self.make_dialogue()
    
    def make_dialogue(self):
        dialogues = []
        self.dialogue_length0 = self.properties['dialogue length0']
        self.dialogue_length1 = self.properties['dialogue length1']
        a=[]
        for i in range(int(self.dialogue_length0)):
            a.append(self.properties['dialogue0'+str(i)])
        dialogues.append(a)
        a=[]
        for i in range(int(self.dialogue_length1)):
            a.append(self.properties['dialogue1'+str(i)])
        dialogues.append(a)
        
        return dialogues
        
class Portal(pg.sprite.Sprite):
    def __init__(self, game, type, x, y, w, h, properties):
        self.groups = game.portals
        pg.sprite.Sprite.__init__(self, self.groups)
        self.name = type
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.properties = properties
        self.dialoguelist = self.make_dialogue()
    
    def make_dialogue(self):
        dialogues = []
        self.dialogue_length0 = self.properties['dialogue length0']
        self.dialogue_length1 = self.properties['dialogue length1']
        a=[]
        for i in range(int(self.dialogue_length0)):
            a.append(self.properties['dialogue0'+str(i)])
        dialogues.append(a)
        a=[]
        for i in range(int(self.dialogue_length1)):
            a.append(self.properties['dialogue1'+str(i)])
        dialogues.append(a)
        return dialogues

class Dialogue(pg.sprite.Sprite):
    def __init__(self, game, type, x, y, w, h, properties):
        self.name = type
        self.groups = game.dialogues
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.properties = properties
        self.dialoguelist = self.make_dialogue()
    
    def make_dialogue(self):
        dialogues = []
        self.dialogue_length0 = self.properties['dialogue length0']
        self.dialogue_length1 = self.properties['dialogue length1']
        a=[]
        for i in range(int(self.dialogue_length0)):
            a.append(self.properties['dialogue0'+str(i)])
        dialogues.append(a)
        a=[]
        for i in range(int(self.dialogue_length1)):
            a.append(self.properties['dialogue1'+str(i)])
        dialogues.append(a)
        
        return dialogues
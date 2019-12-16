import pygame as pg
from settings import *
import time
from chat import *
from sound import *
from quiz import *
from showmap import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, screen, stage):
        # 초기값 설정
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'image')
        self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMGNAME[0][0][0])).convert_alpha()
        self.beforKey = None
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.Beforpos = self.pos
        self.screen = screen
        self.map = Maps(self.screen)
        self.chat = None
        self.chating = False
        self.mapping = False
        self.Mapstage = stage
        self.stupidDegree = 0
        self.direction=0
        self.posdirection=0
        self.beformove = 0
        self.move =0
        self.imgname = 0
        self.stageChk = {
            'quiz' : 0,
            'quiz2' : 0,
            'cloth' : 0,
            'map' : 0,
            'clothPortal' : 0,
            'muscle' : 0,
            'xycar' : 0,
            'teddy' : 0,
        }
        self.stageDialogue = {
            'start' : 0,
            'prologue' : 0,
            'jajus' : 0,
            'teddystart' : 0,
        }
        self.dialogue = {
            'start' : '쿠민',
            'prologue' : '',
            'jajus' : '',
            'teddystart' : '쿠민', 
        }
        self.end=False

    def set_pos(self, x, y):
        # 위치 설정
        self.pos = vec(x, y)
        self.posdirection = self.pos.y
        
    def get_keys(self):
        # 키 입력받기
        self.vel = vec(0, 0)
        self.keys = pg.key.get_pressed()

        if self.chating == False and self.mapping == False:
            if self.keys[pg.K_LEFT] or self.keys[pg.K_a]:
                if self.direction != 1 :
                    self.posdirection=self.pos.x
                    self.direction=1
                self.chkdirection()
                self.vel.x = -PLAYER_SPEED
            elif self.keys[pg.K_RIGHT] or self.keys[pg.K_d]:
                if self.direction != 3 :
                    self.posdirection=self.pos.x
                    self.direction=3
                self.chkdirection()
                self.vel.x = PLAYER_SPEED
            elif self.keys[pg.K_UP] or self.keys[pg.K_w]:
                if self.direction != 2 :
                    self.posdirection=self.pos.y
                    self.direction=2
                self.chkdirection()
                self.vel.y = -PLAYER_SPEED
            elif self.keys[pg.K_DOWN] or self.keys[pg.K_s]:
                if self.direction != 0 :
                    self.posdirection=self.pos.y
                    self.direction=0
                self.chkdirection()
                self.vel.y = PLAYER_SPEED
            elif self.keys[pg.K_SPACE]:
                self.chk_items()
                time.sleep(0.5)
            elif self.keys[pg.K_m]:
                if self.stageChk['map']:
                    self.mapping = True
                    self.map.showMap()
                    pg.display.update()
                    time.sleep(0.3)
                    self.mapping = False
            else :
                self.chkdirection()
            if self.vel.x != 0 and self.vel.y != 0:
                self.vel *= 0.7071
        elif self.chating == True:
            if self.keys[pg.K_f]:
                self.chating = False
            if self.keys[pg.K_SPACE]:
                self.game.draw()
                if self.chat.hasNextPage():
                    self.chat.drawchat()
                    time.sleep(0.5)
                else:
                    self.chating = False
                    time.sleep(0.2)
        elif self.mapping:
            pass

        self.beforKey = self.keys

    def chkdirection(self):
        if self.direction == 1 or self.direction == 3:
            num = int((abs(self.posdirection-self.pos.x)//25)%4)
            self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMGNAME[self.imgname][self.direction][num])).convert_alpha()
        if self.direction == 0 or self.direction == 2:
            num = int((abs(self.posdirection-self.pos.y)//25)%4)
            self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMGNAME[self.imgname][self.direction][num])).convert_alpha()
        if self.beformove == num and num!=0:
            self.move+=1
            self.beformove = num
        else :
            self.move = 0
            self.beformove = num
        if self.move > 60 :
            if self.direction == 1 or self.direction == 3:
                self.posdirection = self.pos.x
            else :
                self.posdirection = self.pos.y
            self.move = 0

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
        # space bar 클릭시 item 유무 확인 및 상호작용
        hits = pg.sprite.spritecollide(self, self.game.items, False)
        if hits:
            set_sfx(SOUNDEFFECT_LIST[0])
            for sprite in hits:
                if sprite.name == 'quiz':
                    chat = [['철컥하는 소리가 들린다. 어딘가 열린 것 같다.'],['비웃는 소리가 들린다.']]
                    self.chatmake(sprite.dialoguelist, self.stageChk[sprite.name])
                    self.chating = True
                    if self.stageChk[sprite.name] == 0:
                        self.quiz = Quiz(self.screen, self.game, sprite.properties['answer'],chat)
                        self.quiz.startQuiz()
                    if self.quiz.solve:
                        self.stageChk[sprite.name] = 1
                if sprite.name == 'quiz2':
                    chat = [['7호관 정문 열쇠를 얻었다.'],['비웃는 소리가 들린다.']]
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk[sprite.name])
                    if self.stageChk[sprite.name] == 0:
                        self.quiz = Quiz(self.screen, self.game, sprite.properties['answer'],chat)
                        self.quiz.startQuiz()
                    if self.quiz.solve:
                        self.stageChk[sprite.name] = 1
                elif sprite.name == 'cloth':
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk[sprite.name])
                    if self.stageChk['cloth'] == 0:
                        self.imgname = 1
                        self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMGNAME[self.imgname][self.direction][0])).convert_alpha()
                    self.stageChk[sprite.name] = 1
                elif sprite.name == 'basin':
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk['cloth'], '쿠민')
                    if self.stageChk['cloth'] == 0:
                        self.imgname = 2
                        self.image = pg.image.load(os.path.join(self.img_folder, PLAYER_IMGNAME[self.imgname][self.direction][0])).convert_alpha()
                    self.stageChk['cloth'] = 1
                elif sprite.name == 'strong' :
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, 0)
                    self.stageChk['muscle'] = 1
                elif sprite.name == 'xycar' :
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk['xycar'])
                    if self.stageChk['xycar'] == 0:
                        for sprit in self.game.npcs:
                            if sprite.name == 'xycar':
                                self.game.npcs.chk=1
                                break
                    self.stageChk['xycar']=1
                elif sprite.name == 'map':
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk[sprite.name])
                    self.stageChk[sprite.name] = 1
                elif sprite.name == 'teddy':
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageChk[sprite.name])
                    self.stageChk[sprite.name] = 1
                else :
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, 0)
        else:
            chatting = [['멍청하게 시간을 날리고 있다.'],['걷는건 space가 아니라 w키다'],['bug인가?'],['그만해 이제 대사없어']]
            self.chating = True
            self.chatmake(chatting, self.stupidDegree)
            self.stupidDegree+=1
            self.stupidDegree%=len(chatting)

    def chk_potal(self):
        # 캐릭터의 위치와 포탈의 위치 비교
        hits = pg.sprite.spritecollide(self, self.game.portals, False)
        if hits and self.chating == False:
            for sprite in hits:
                if sprite.name == 'fitness' :
                    if self.stageChk['cloth'] == 0:
                        self.pos = self.Beforpos
                        self.pos.y-=20
                        self.chatmake(sprite.dialoguelist, self.stageChk['clothPortal'])
                        self.chating = True
                        time.sleep(0.2)
                        if self.stageChk['clothPortal']==0:
                            self.stageChk['clothPortal']=1
                    else:
                        set_sfx(SOUNDEFFECT_LIST[1])
                        self.Mapstage=PORTALMAP[sprite.name]
                elif sprite.name == 'secondfloor' :
                    if self.stageChk['muscle'] == 0:
                        set_sfx(SOUNDEFFECT_LIST[4])
                        self.pos = self.Beforpos
                        self.pos.x+=20
                        self.chatmake(sprite.dialoguelist, 0)
                        self.chating = True
                        time.sleep(0.2)
                    elif self.stageChk['muscle'] == 1:
                        set_sfx(SOUNDEFFECT_LIST[2])
                        self.chatmake(sprite.dialoguelist, 1)
                        self.chating = True
                        time.sleep(1)
                        self.Mapstage=PORTALMAP[sprite.name]
                        self.stageChk['muscle']=2
                    else :
                        set_sfx(SOUNDEFFECT_LIST[5])
                        self.Mapstage=PORTALMAP[sprite.name]
                elif sprite.name == 'shower':
                    set_sfx(SOUNDEFFECT_LIST[1])
                    self.Mapstage=PORTALMAP[sprite.name]
                elif sprite.name == 'jajus':
                    if self.stageChk['quiz'] == 1:
                        set_sfx(SOUNDEFFECT_LIST[5])
                        self.Mapstage=PORTALMAP[sprite.name]
                    else :
                        self.pos = self.Beforpos
                        if self.direction == 0 :
                            self.pos.y-=20
                        if self.direction == 1 :
                            self.pos.x+=20
                        if self.direction == 2 :
                            self.pos.y+=20
                        if self.direction == 3 :
                            self.pos.x-=20
                        self.chating = True
                        self.chatmake(sprite.dialoguelist, self.stageChk['quiz'])
                elif sprite.name == '444':
                    if self.stageChk['xycar'] == 1:
                        set_sfx(SOUNDEFFECT_LIST[5])
                        self.Mapstage=PORTALMAP[sprite.name]
                    else :
                        self.pos = self.Beforpos
                        if self.direction == 0 :
                            self.pos.y-=20
                        if self.direction == 1 :
                            self.pos.x+=20
                        if self.direction == 2 :
                            self.pos.y+=20
                        if self.direction == 3 :
                            self.pos.x-=20
                        self.chating = True
                        self.chatmake(sprite.dialoguelist, self.stageChk['xycar'])
                elif sprite.name == 'none' :
                    self.pos = self.Beforpos
                    if self.direction == 0 :
                        self.pos.y-=20
                    if self.direction == 1 :
                        self.pos.x+=20
                    if self.direction == 2 :
                        self.pos.y+=20
                    if self.direction == 3 :
                        self.pos.x-=20
                    self.chatmake(sprite.dialoguelist, 0)
                    self.chating = True
                    time.sleep(0.2)
                elif sprite.name == 'end' :
                    if self.stageChk['quiz2']==0:
                        self.pos = self.Beforpos
                        if self.direction == 0 :
                            self.pos.y-=20
                        if self.direction == 1 :
                            self.pos.x+=20
                        if self.direction == 2 :
                            self.pos.y+=20
                        if self.direction == 3 :
                            self.pos.x-=20
                        self.chating = True
                        self.chatmake(sprite.dialoguelist, 0)
                    else :
                        if self.stageChk['teddy']==0:
                            self.pos = self.Beforpos
                            if self.direction == 0 :
                                self.pos.y-=20
                            if self.direction == 1 :
                                self.pos.x+=20
                            if self.direction == 2 :
                                self.pos.y+=20
                            if self.direction == 3 :
                                self.pos.x-=20
                            self.chating = True
                            self.chatmake(sprite.dialoguelist, 1)
                        else :
                            self.pos = self.Beforpos
                            if self.direction == 0 :
                                self.pos.y-=20
                            if self.direction == 1 :
                                self.pos.x+=20
                            if self.direction == 2 :
                                self.pos.y+=20
                            if self.direction == 3 :
                                self.pos.x-=20
                            set_sfx(SOUNDEFFECT_LIST[5])
                            chat = [['철컥소리와 함께 문이 열렸다.']]
                            self.chating = True
                            self.chatmake(chat, 0)
                            self.end=True
                else:
                    set_sfx(SOUNDEFFECT_LIST[5])
                    self.Mapstage=PORTALMAP[sprite.name]
        else:
            self.Beforpos = self.pos
    
    def chkdialogue(self):
        # 대화가 있는지 확인
        hits = pg.sprite.spritecollide(self, self.game.dialogues, False)
        if hits:
            for sprite in hits:
                if self.stageDialogue[sprite.name] == 0:
                    if sprite.name == 'jajus':
                        set_sfx(SOUNDEFFECT_LIST[7])
                    self.chating = True
                    self.chatmake(sprite.dialoguelist, self.stageDialogue[sprite.name], self.dialogue[sprite.name])
                    time.sleep(0.2)
                    self.stageDialogue[sprite.name]=1
    
    def chknpc(self):
        hits = pg.sprite.spritecollide(self, self.game.npcs, False)
        direction_list = [vec(0,-NPC_KNOCKBACK),vec(NPC_KNOCKBACK,0),vec(0, NPC_KNOCKBACK),vec(-NPC_KNOCKBACK,0)]
        chatting = [['뭐야 안비켜?']]
        if hits:
            for sprite in hits:
                if sprite.name == 'xycar':
                    sprite.npcpause()
                    set_sfx(SOUNDEFFECT_LIST[6])
                    self.pos += direction_list[self.direction]
                    self.chating = True
                    self.chatmake(chatting, 0, '???')
                    sprite.npcpause()
    
    def chatmake(self, dialogue, num, name=''):
        self.chat = Chat(self.screen, dialogue, num, name)
        self.chat.drawchat()

    def update(self):
    #캐릭터 위치 업데이트
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.chk_walls('x')
        self.rect.y = self.pos.y
        self.chk_walls('y')
        self.chknpc()
        self.chk_potal()
        self.chkdialogue()

class NPC(pg.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.groups = game.all_sprites, game.npcs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = type
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'image')
        self.image = pg.image.load(os.path.join(self.img_folder, NPC_IMGNAME[0][0])).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.sleep = 0
        self.chk = 0
        self.direction=0
        self.pause = False

    def chk_walls(self, dir):
        #캐릭터를 움직이기 전에 벽이 있는지 확인
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.npcwalls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.npcwalls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                    self.direction = 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                    self.direction = 0
                self.vel.y = 0
                self.rect.y = self.pos.y

    def chkmove(self):
        if self.pause == False :
            self.vel = vec(0, 0)
            if self.direction == 2:
                self.vel.y = -NPC_SPEED
            else :
                self.vel.y = NPC_SPEED
            if self.vel.x != 0 and self.vel.y != 0:
                    self.vel *= 0.7071

    def npckill(self):
        self.kill()

    def npcpause(self):
        self.pause = not self.pause

    def update(self):
        if self.sleep>50:
            self.chkmove()
        else :
            self.sleep +=1
        if self.pause == False :
            self.pos += self.vel * self.game.dt
            self.rect.x = self.pos.x
            self.chk_walls('x')
            self.rect.y = self.pos.y
            self.chk_walls('y')
            self.image = pg.image.load(os.path.join(self.img_folder, NPC_IMGNAME[self.chk][self.direction])).convert_alpha()

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

class npcWall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.npcwalls
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
        #tmx에 dialogues를 list로 변경
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
    
    def update(self):
        if self.name == 'xycar':
            for sprite in self.game.npcs:
                if(sprite.name == 'xycar'):
                    self.rect.x = sprite.rect.x-15
                    self.rect.y = sprite.rect.y-15
                    break
        
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
        #tmx에 dialogues를 list로 변경
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
        #tmx에 dialogues를 list로 변경
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
import pygame as pg
import sys, pytmx, time
from os import path
from settings import *
from sprites import *
from tilemap import *
from sound import *

class Game:
    def __init__(self):
        # 초기 설정값
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.mapStage = 0
        self.beforStage = 0
        self.paused = False
        self.mapname = 'start'

        self.shadow = pg.Surface((WIDTH, HEIGHT))
        self.shadow.fill(SHADOW_COLOR)
        self.shadow_mask = pg.image.load(path.join('image', LIGHTMASK)).convert_alpha()
        self.shadow_mask = pg.transform.scale(self.shadow_mask, LIGHT_RADIUS)
        self.shadow_rect = self.shadow_mask.get_rect()

        pg.mixer.init()

        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 0, 0, self.screen, self.mapStage)
        self.load_data()

    def load_data(self):
        # 게임의 이미지 정보 로드
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, STAGETMX[self.mapStage]))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        # 게임의 sprite 그룹 정의 및 플레이어 위치 설정
        self.walls = pg.sprite.Group()
        self.npcwalls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        self.portals = pg.sprite.Group()
        self.dialogues = pg.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)
        cnt = 0
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                if tile_object.type == 'escape':
                    self.player.escape = vec(tile_object.x, tile_object.y)
                if tile_object.type == self.mapname and cnt ==0:
                    cnt+=1
                    self.player.set_pos(tile_object.x, tile_object.y)
                    if tile_object.type == 'start' :
                        self.mapname = 'shower'
            if tile_object.name == 'npc':
                NPC(self, tile_object.x, tile_object.y, tile_object.type)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name == 'npcwall':
                npcWall(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name == 'item':
                Item(self,tile_object.type, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height, tile_object.properties)
            if tile_object.name == 'portal':
                Portal(self,tile_object.type, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height, tile_object.properties)
            if tile_object.name == 'dialogue':
                Dialogue(self,tile_object.type, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height, tile_object.properties)

    def run(self):
        # 게임 동작
        self.playing = True
        set_music(SOUNDLIST[0])
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            if self.player.end==True : self.ending()
            self.events()
            if self.mapStage!=self.player.Mapstage:
                self.mapStage = self.player.Mapstage
                for sprite in self.npcs :
                    sprite.npckill()
                self.load_data()
                self.new()
                self.mapname = STAGENAME[self.mapStage]
            if not self.paused :
                self.update()
            if not self.player.chating:
                self.draw()

    def update(self):
        # 게임 카메라, sprites update  
        self.all_sprites.update()
        self.items.update()
        self.camera.update(self.player)

    def draw(self):
        #스크린 draw
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.render_shadow()
        pg.display.flip()

    def events(self):
        # 키 이벤트 처리
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def wait(self):
        #키 입력 대기
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    return

    def startscreen(self):
        set_music(SOUNDLIST[2])
        Image = []
        for i in STARTIMAGE:
            Image.append(pg.image.load(path.join(STARTIMAGE_DIR, i)))
        
        cnt = 0
        running = True
        while running:
            self.screen.blit(Image[cnt%4], self.rect)
            pg.display.update()
            cnt+=1
            time.sleep(0.7)
            for event in pg.event.get():# User did something
                if event.type == pg.KEYDOWN:
                    running = False

    def prologue(self):
        #prologue screen

        #SCENE1
        set_music(SOUNDLIST[1])
        pImage = []
        fps = 1
        prologue1_dir = os.path.join(PROLOGUEIMAGE_DIR, "scene1")
        prologueimage = os.listdir(prologue1_dir)
        for i in prologueimage:
            pImage.append(pg.image.load(path.join(prologue1_dir, i)))
        
        for i in range(len(pImage)) :
            self.screen.blit(pImage[i], self.rect)
            pg.display.update()
            if i == 1:
                set_sfx('thing.ogg')
            if i == 2:
                fps = 0.2
            elif i == 9:
                fps = 1
            elif i == 10:
                set_sfx('humming.ogg')
            elif i == 12:
                fps = 0.3
            elif i == 15:
                fps = 1
            elif i == 16:
                fps = 0.3
            time.sleep(fps)
        
        #SCENE2
        pImage = []
        fps =  0.4
        prologue1_dir = os.path.join(PROLOGUEIMAGE_DIR, "scene2")
        prologueimage = os.listdir(prologue1_dir)
        for i in prologueimage:
            pImage.append(pg.image.load(path.join(prologue1_dir, i)))

        for i in range(len(pImage)):
            self.screen.blit(pImage[i], self.rect)
            pg.display.update()
            if i==6:
                set_sfx('dooropen.ogg')
            elif i==9:
                fps = 1
            elif i==11:
                fps = 0.5
            elif i==13:
                set_sfx('curtain.ogg')
            elif i==14:
                fps = 0.5
                time.sleep(0.2)
            time.sleep(fps)

        #scene3
        pImage = []
        fps =  0.6
        prologue1_dir = os.path.join(PROLOGUEIMAGE_DIR, "scene3")
        prologueimage = os.listdir(prologue1_dir)
        for i in prologueimage:
            pImage.append(pg.image.load(path.join(prologue1_dir, i)))
        for i in range(len(pImage)):
            self.screen.blit(pImage[i], self.rect)
            pg.display.update()
            if i==0:
                set_music('shower.ogg')
            elif i == 6:
                set_sfx('thing.ogg', volume=0.7)
                time.sleep(0.7)
            elif i == 14:
                time.sleep(0.1)
                set_music('horror.ogg')
                fps = 2
            elif i==15:
                set_sfx('switch.ogg')
            elif i == 16:
                set_sfx('her.ogg')
                time.sleep(0.5)
            time.sleep(fps)

        time.sleep(0.2)
        self.screen.fill(BLACK)

    def ending(self):
        #game ending
        shadowimg = pg.image.load(os.path.join(IMAGE_DIR, 'black2.png'))
        pImage = []
        fps =  0.5
        ending_dir = os.path.join(ENDINGIMG_DIR, "scene")
        endingimage = os.listdir(ending_dir)
        for i in endingimage:
            pImage.append(pg.image.load(path.join(ending_dir, i)))

        pg.mixer.stop()
        set_music('home.ogg', volume=0.3)
        for i in range(len(pImage)):
            self.screen.blit(pImage[i], self.rect)
            pg.display.update()
            if i == 8:
                set_sfx('foot.ogg')
                pg.mixer.music.set_volume(0.2)
                fps = 0.3
            elif i == 19:
                fps=1
                pg.mixer.music.fadeout(600)
            elif i == 21:
                pg.mixer.stop()
                set_sfx('onlight.ogg')
                time.sleep(0.3)
                fps = 0.5
            elif i== 22:
                time.sleep(0.5)
                pg.mixer.stop()
                set_sfx('ramen.ogg', volume=0.2)
            elif i==28:
                pg.mixer.fadeout(500)

            time.sleep(fps)
        for i in range(10):
                self.screen.blit(shadowimg, self.rect)
                pg.display.update()
                time.sleep(0.1)
        time.sleep(0.2)
        pg.mixer.stop()
        
        set_music('credit.ogg', volume=0.6)
        time.sleep(1)

        shadowimg = pg.image.load(os.path.join(IMAGE_DIR, 'black2.png'))
        pImage = []

        credit_dir = os.path.join(ENDINGIMG_DIR, "credit")
        creditimage = os.listdir(credit_dir)
        for i in creditimage:
            pImage.append(pg.image.load(path.join(credit_dir, i)))

        self.screen.fill(BLACK)

        fps = 2

        for i in range(len(pImage)):
            set_sfx('switch.ogg')
            self.screen.blit(pImage[i], self.rect)
            pg.display.update()
            time.sleep(3)
            for i in range(6):
                self.screen.blit(shadowimg, self.rect)
                pg.display.update()
                time.sleep(0.1)
            if i == 3:
                fps = 1.5
                pg.mixer.music.fadeout(400) 
            time.sleep(fps)
        pg.mixer.music.fadeout(600)
        pg.mixer.stop()
        time.sleep(1)
        pg.quit()
        sys.exit()

    def render_shadow(self):
        #player shadow render
        self.shadow.fill(SHADOW_COLOR)
        self.shadow_rect.center = self.camera.apply(self.player).center
        self.shadow.blit(self.shadow_mask, self.shadow_rect)
        self.screen.blit(self.shadow, (0,0), special_flags = pg.BLEND_MULT)
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
        self.items = pg.sprite.Group()
        self.portals = pg.sprite.Group()
        self.dialogues = pg.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)
        cnt = 0
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                if tile_object.type == self.mapname and cnt ==0:
                    cnt+=1
                    self.player.set_pos(tile_object.x, tile_object.y)
                    if tile_object.type == 'start' :
                        self.mapname = 'shower'
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y,
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
            self.events()
            if self.mapStage!=self.player.Mapstage:
                self.mapStage = self.player.Mapstage
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

    def prologue(self):
        #prologue screen
        set_music(SOUNDLIST[3])
        start = False
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        pImage = []
        for i in TUTORIALIMAGE:
            pImage.append(pg.image.load(path.join(img_folder, i)))
        begin_image = pg.image.load(path.join(img_folder, STARTIMAGE))
        black_image = pg.image.load(path.join(img_folder, PAGEBLACK))

        self.screen.blit(begin_image ,self.rect)
        pg.display.update()
        self.wait()
            
        for img in pImage :
            self.screen.blit(img ,self.rect)
            pg.display.update()
            time.sleep(0.5)
            self.wait()

        for i in range(13):
            self.screen.blit(black_image, self.rect)
            pg.display.update()
            time.sleep(0.04)
        pg.mixer.music.stop()

    def ending(self):
        #game ending
        pass

    def render_shadow(self):
        #player shadow render
        self.shadow.fill(SHADOW_COLOR)
        self.shadow_rect.center = self.camera.apply(self.player).center
        self.shadow.blit(self.shadow_mask, self.shadow_rect)
        self.screen.blit(self.shadow, (0,0), special_flags = pg.BLEND_MULT)
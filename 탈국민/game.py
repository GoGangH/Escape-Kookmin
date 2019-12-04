import pygame as pg
import sys, pytmx, time
from os import path
from settings import *
from sprites import *
from tilemap import *
from sound import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.mapStage = 0
        self.beforStage = 0
        self.paused = False
        self.mapname = 'start'
        pg.mixer.init()

        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 0, 0, self.screen, self.mapStage)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, STAGETMX[self.mapStage]))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        #self.items_dict = {}
        self.portals = pg.sprite.Group()
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
                item = Item(self,tile_object.type, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height, tile_object.properties)
                #self.items_dict[tile_object.name] = item
                #self.test_item = item
            if tile_object.name == 'portal':
                Portal(self,tile_object.type, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height, tile_object.properties)

    def run(self):
        # game loop - set self.playing = False to end the game
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
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        #스크린 draw
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
        #tutorial screen
        set_music(SOUNDLIST[0])
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
        pass
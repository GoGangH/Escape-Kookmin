import pygame as pg
import os, sys
from settings import *
from sound import *
from sound import *

class Maps:
    def __init__(self, screen, index=0):
        self.screen = screen
        self.mapnum = index #0=2F 1=4F
        self.mapimg = pg.image.load(os.path.join(MAPIMG_DIR, MAPIMGLIST[self.mapnum]))
        self.mapimg_rect = self.mapimg.get_rect()
        self.rarrow = pg.image.load(os.path.join(IMAGE_DIR, 'rarrow.png'))
        self.rarrow_rect = self.rarrow.get_rect()
        self.larrow = pg.image.load(os.path.join(IMAGE_DIR, 'larrow.png'))
        self.larrow_rect = self.larrow.get_rect()
        self.showing = False

    def updateMapimg(self):
        self.mapimg = pg.image.load(os.path.join(MAPIMG_DIR, MAPIMGLIST[self.mapnum]))

    def drawMap(self):
        self.screen.blit(self.mapimg, self.mapimg_rect)
        
    def drawArrow(self):
        if self.mapnum == 0:
            self.screen.blit(self.rarrow, self.rarrow_rect)
        else:
            self.screen.blit(self.larrow, self.larrow_rect)

    def get_keys(self):
        answering = True
        while answering:
            for evt in pg.event.get():
                if evt.type == pg.KEYDOWN:
                    if evt.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif evt.key == pg.K_m:
                        answering = False
                    if self.mapnum == 0:
                        if evt.key == pg.K_RIGHT:
                            self.mapnum = 1
                            self.updateMapimg()
                            self.drawMap()
                            self.drawArrow()
                            pg.display.update()
                    else:
                        if evt.key == pg.K_LEFT:
                            self.mapnum = 0
                            self.updateMapimg()
                            self.drawMap()
                            self.drawArrow()
                            pg.display.update()

    def showMap(self):
        self.updateMapimg()
        self.drawMap()
        self.drawArrow()
        pg.display.update()
        self.get_keys()

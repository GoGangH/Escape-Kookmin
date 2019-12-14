import pygame as pg
import os
from settings import *
from sound import *

class Chat:
    def __init__(self, screen, dialogue, index, chat=''):
        self.chatter = chat
        self.screen = screen
        self.backgroundimg = pg.image.load(os.path.join(CHAT_DIR, CHAT_IMG))
        self.chatterimg = pg.image.load(os.path.join(CHAT_DIR, CHATTER_IMG))
        self.chatRect = self.backgroundimg.get_rect()
        self.chatterRect = self.chatterimg.get_rect()
        self.font = pg.font.Font(MAINFONT, 18)
        self.indexX = index
        print(self.indexX)
        self.indexY = 0
        self.dialogue = dialogue

    def drawback(self):
        self.screen.blit(self.backgroundimg, self.chatRect)

    def drawchatter(self):
        self.screen.blit(self.chatterimg, self.chatterRect)

    def drawText(self):
        # 대화창속 텍스트 설정
        textobj = self.font.render(self.chatter, True, BLACK)
        textrect = textobj.get_rect()
        textrect.x = 42
        textrect.y = 396
        self.screen.blit(textobj, textrect)
        textobj = self.font.render(self.dialogue[self.indexX][self.indexY], True, BLACK)
        textrect = textobj.get_rect()
        textrect.x = 42
        textrect.y = 450
        self.screen.blit(textobj, textrect)

    def drawchat(self):
        '''chat 그리기'''
        if self.chatter != '':
            self.drawchatter()
        self.drawback()
        self.drawText()
        self.indexY += 1
        pg.display.update()

    def hasNextPage(self):
        '''더 넘길 대화창이 있는지 확인'''
        if self.indexY >= len(self.dialogue[self.indexX]):
            return False
        else:
            return True
import pygame as pg
import os
from settings import *
from sound import *

class Chat:
    def __init__(self, screen, dialogue, index=0, chat=''):
        game_dir = os.path.dirname(__file__)
        chat_dir = os.path.join(game_dir, 'chat')
        self.chatter = chat
        self.screen = screen
        self.chat_img = pg.image.load(os.path.join(chat_dir, CHAT_IMG))
        self.chatRect = self.chat_img.get_rect()
        self.chatRect.centerx = CHAT_WIDTH
        self.chatRect.top = CHAT_HEIGHT
        self.font = pg.font.Font('font\\HMFMMUEX.TTC', 14)
        self.indexX = index
        self.indexY = 0
        self.dialogue = dialogue
        self.image = self.chating()
        self.chkChat = chat

    def chating(self):
        self.screen.blit(self.chat_img, self.chatRect)

    def drawText(self):
        # 대화창속 텍스트 설정
        textobj = self.font.render(self.chatter, True, WHITE)
        textrect = textobj.get_rect()
        textrect.centerx = CHAT_WIDTH-170
        textrect.centery = 50
        self.screen.blit(textobj, textrect)
        textobj = self.font.render(self.dialogue[self.indexX][self.indexY], True, BLACK)
        textrect = textobj.get_rect()
        textrect.centerx = self.chatRect.centerx
        textrect.centery = self.chatRect.centery
        self.screen.blit(textobj, textrect)
        textBoxImage = pg.image.load('chat\\textBox.png')
        textBoxRect = textBoxImage.get_rect()
        textBoxRect.topleft = (0,WIDTH-textBoxRect.height)

    def drawchat(self):
        # chat 그리기
        self.chating()
        self.drawText()
        self.indexY += 1
        pg.display.update()

    def hasNextPage(self):
        '''더 넘길 대화창이 있는지 확인'''
        if self.indexY >= len(self.dialogue[self.indexX]):
            return False
        else:
            return True
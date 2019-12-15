import pygame as pg
import os, sys
from settings import *
from sound import *
from chat import *
from sound import *

class Quiz:
    def __init__(self, screen, game, quizanswer, dialogue):
        self.screen = screen
        self.answer = quizanswer
        self.enter_img = pg.image.load(os.path.join(QUIZ_DIR, ENTER_IMG))
        self.quiz_img = pg.image.load(os.path.join(QUIZ_DIR, quizanswer+'.png'))
        self.enter_rect = self.enter_img.get_rect()
        self.quiz_rect = self.enter_img.get_rect()
        self.font = pg.font.Font(CODEFONT, 18)
        self.scorefont = pg.font.Font(MAINFONT, 18)
        self.text = self.font.render('', True, BLACK)
        self.current_string = ""
        self.quizplay = False
        self.chat = None
        self.solve = False
        self.dialogue = dialogue
    
    def drawEnter(self):
        self.screen.blit(self.enter_img, self.enter_rect)

    def drawQuiz(self):
        self.screen.blit(self.quiz_img, self.quiz_rect)

    def drawText(self):
        self.text = self.font.render(self.current_string + "_", True, BLACK)
        textrect = self.text.get_rect()
        textrect.x = 149
        textrect.y = 468.5
        self.screen.blit(self.text, textrect)

    def get_answer(self):
        answering = True
        self.current_string.lstrip()
        while answering:
            for evt in pg.event.get():
                if evt.type == pg.KEYDOWN:
                    if evt.key == pg.K_BACKSPACE:
                        if len(self.current_string) > 0:
                            self.current_string = self.current_string[:-1]
                            self.drawEnter()
                            self.drawText()
                            pg.display.update()
                    if evt.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif evt.key == pg.K_RETURN or evt.key == pg.K_KP_ENTER:
                        self.current_string.lstrip()
                        self.drawQuiz()
                        answering = False
                    elif evt.unicode.isalpha() or evt.unicode.isnumeric() or evt.unicode in SYMBOLS:
                        self.current_string += evt.unicode
                        self.drawEnter()
                        self.drawText()
                        pg.display.update()

    def isCorrect(self):
        self.current_string = self.current_string.strip()
        if self.answer == self.current_string:
            return True
        else:
            return False

    def drawCorrect(self):
        if not self.isCorrect():
            incorrect = self.scorefont.render("틀렸습니다.", True, RED)
            incorrect_rect = incorrect.get_rect()
            incorrect_rect.centerx = 698
            incorrect_rect.centery = 396.5
            self.screen.blit(incorrect, incorrect_rect)
        else:
            correct = self.scorefont.render("맞았습니다.", True, GREEN)
            correct_rect = correct.get_rect()
            correct_rect.centerx = 698
            correct_rect.centery = 396.5
            self.screen.blit(correct, correct_rect)

    def startQuiz(self):
        self.quizplay = True
        while self.quizplay:
            self.screen.fill(BLACK)
            self.drawQuiz()
            self.drawEnter()
            self.drawText()
            self.get_answer()
            if self.isCorrect():
                self.chat = Chat(self.screen, self.dialogue, 0)
                self.chat.drawchat()
                self.solve=True
            else:
                set_sfx('fun.mp3')
                self.chat = Chat(self.screen, self.dialogue, 1)
                self.chat.drawchat()
            self.quizplay = False
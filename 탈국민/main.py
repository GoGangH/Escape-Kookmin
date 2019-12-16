import pygame as pg
import sys, os
from settings import *
from sprites import *
from game import *

g = Game()
g.startscreen() 
g.prologue()
while True:
    g.new()
    g.run()
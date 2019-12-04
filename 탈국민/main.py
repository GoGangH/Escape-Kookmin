import pygame as pg
import sys, os
from settings import *
from sprites import *
from game import *

g = Game()
while True:
    g.new()
    g.run()
    g.ending()
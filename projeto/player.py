import pygame as pg
from configs import *

class Player(pg.sprite.Sprite):
    
    def __init__(self, game, spawn_x, spawn_y):

        self.game = game
        
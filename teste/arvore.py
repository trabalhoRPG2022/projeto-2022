from turtle import pos
import pygame as pg
from configs import *

class Arvore(pg.sprite.Sprite):
    def __init__(self,pos, groups) -> None:
        super().__init__(groups)
        self.image = pg.image.load('img/arvore1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.image.set_colorkey(branco)
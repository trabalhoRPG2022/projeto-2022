import pygame as pg
from configs import *

class Player(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = 44
        self.height = 61

        self.x_change = 0
        self.y_change = 0

        self.image = pg.Surface([self.width, self.height])
        self.image.fill(vermeho)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        image = pg.image.load('img\personagemprincipal.png')

        self.image = pg.Surface([self.width, self.height])
        self.image.set_colorkey(verde)
        self.image.blit(image, (0,0))
        

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.x_change -= speed

        if keys[pg.K_d]: 
            self.x_change += speed    
    
        if keys[pg.K_w]:    
            self.y_change -= speed 

        if keys[pg.K_s]: 
            self.y_change += speed
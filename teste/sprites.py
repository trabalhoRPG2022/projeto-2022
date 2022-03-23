from re import S
from tkinter import W, Widget
import pygame as pg
import math
import random
from configs import *


class Sprite_sheet:
    def __init__(self, file) -> None:
        self.sheet = pg.image.load(file).convert()
    
    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(branco)
        return sprite

class Sprite_sheet2:
    def __init__(self, file) -> None:
        self.sheet = pg.image.load(file).convert()
    
    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(preto)
        return sprite


class Player(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        self.mostrar_chao = pg.display.get_surface()
        self.obstaculos_visiveis = pg.sprite.Group()
        self.obstaculos = pg.sprite.Group()
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
        
        
        self.image = self.game.character_spritesheet.get_sprite(152, 9, self.width, self.width)

        

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x +=  speed
            self.x_change -= speed
            self.facing = 'right'

        if keys[pg.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -=  speed
            self.x_change += speed    
    
        if keys[pg.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y +=  speed 
            self.y_change -= speed 

        if keys[pg.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -=  speed
            self.y_change += speed
                    
    
    def run(self):
        self.obstaculos_visiveis.draw(self.mostrar_chao)

class Arvore(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image = self.game.terreno_spritesheet.get_sprite(285, 872, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Fundo(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = fundo_layer
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image  = self.game.terreno_spritesheet.get_sprite(165, 324 , self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Void(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = fundo_layer
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image  = self.game.terreno_spritesheet.get_sprite(495, 925 , self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Casa_chao(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = fundo_layer
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image  = self.game.terreno_spritesheet.get_sprite(367, 759 , self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class monitor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image  = self.game.terreno_spritesheet.get_sprite(297, 1088 , self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
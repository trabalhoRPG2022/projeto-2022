import pygame as pg
from configs import *
from arvore import Arvore


class Player(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        self.mostrar_chao = pg.display.get_surface()
        self.obstaculos_visiveis = pg.sprite.Group()
        self.obstaculos = pg.sprite.Group()
        pg.sprite.Sprite.__init__(self, self.groups)
        self.criar_mapa()


        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.x_change = 0
        self.y_change = 0

        self.image = pg.Surface([self.width, self.height])
        self.image.fill(vermeho)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

        image = pg.image.load('img/personagem.png')
        
        self.image = pg.Surface([self.width, self.height])
        self.image.set_colorkey(preto)
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
        
    def criar_mapa(self):
        for obs_index,obs in enumerate(MAPA_MUNDO):
            for coluna_index, coluna in enumerate(obs):
                x =  coluna_index * tile_size
                y =  obs_index * tile_size
                if coluna == 'x':
                    Arvore((x,y), [self.obstaculos_visiveis])
                    
    
    def run(self):
        self.obstaculos_visiveis.draw(self.mostrar_chao)

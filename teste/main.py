import pygame as pg
from sprites import *
from configs import *


class Game:

    def __init__(self):
        pg.init()
        self.background = pg.display.set_mode((largura, altura))
        self.clock = pg.time.Clock()
        self.rodando = True

        self.character_spritesheet = Sprite_sheet("img/persona.png")
        self.terreno_spritesheet = Sprite_sheet("img/map.png")


    def criar_mapa(self):
        for i, row in enumerate(MAPA_MUNDO):
            for j, column in enumerate(row):
                Fundo(self, j, i)
                if column == 'x':
                    Arvore(self, j, i)

        
    def new(self):
        self.sair = True

        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.enemies = pg.sprite.LayeredUpdates()
        self.attacks = pg.sprite.LayeredUpdates()
        self.player = Player(self, 7, 6)
        self.criar_mapa()

    def eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.rodando = False
                self.sair = False

    def atualizacoes(self):
        self.all_sprites.update()
        self.all_sprites.draw(self.background)
        self.clock.tick(FPS)
        pg.display.update()

    def draw(self):
        self.background.blit(pg.image.load('img\chaoquadriculado.png'), (0,0))

    def main(self):
        while self.sair:
            self.eventos()
            self.atualizacoes()
            self.player.run()
        self.rodando = False

game = Game()
game.new()
while game.rodando:
    game.main()
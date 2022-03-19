from configs import *
import pygame as pg


class Jogo:

    def __init__(self):
        pg.init()
        
        self.background = pg.display.set_mode(resolucao)
        pg.display.set_caption('RPG')

        self.sair = True
        self.jogando = True

        self.pos_x = meio_x
        self.pos_y = meio_y

    def main(self):
        while self.jogando:
            self.eventos()
            self.personagem()
            self.movimento()
            
    def eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.jogando = False
                self.sair = False
            pg.display.update()

    def personagem(self):
        self.background.fill(cor_branco)
        pg.draw.rect(self.background, cor_vermelho, (self.pos_x, self.pos_y, width, height))

    def movimento(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.pos_x -= vel

        if keys[pg.K_d]: 
            self.pos_x += vel     
    
        if keys[pg.K_w]:    
            self.pos_y -= vel 

        if keys[pg.K_s]: 
            self.pos_y += vel

    def update(self):
        pg.display.update()

jogo = Jogo()

while jogo.sair:
    jogo.main()
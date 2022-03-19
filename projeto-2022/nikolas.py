import pygame as pg


#lugar onde estão sendo definidas as variaveis mais importantes do jogo
resolucao = (1200, 800)
x = 500
y = 500
width = 20
height = 20
vel = 2
sair = True

#configs do display
background = pg.display.set_mode(resolucao)
pg.display.set_caption('RPG')

while sair:

    #este loop é responsável por captar quando o usuário clica no botao de fechar e fecha o jogo
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sair = False

    keys = pg.key.get_pressed() 
      
    
    if keys[pg.K_LEFT]:   
        x -= vel  
    
    if keys[pg.K_RIGHT]: 
        x += vel      
    
    if keys[pg.K_UP]:    
        y -= vel 
          
    if keys[pg.K_DOWN]: 
        y += vel     
    
    background.fill((255, 255, 255)) 
      
    pg.draw.rect(background, (255, 0, 0), (x, y, width, height)) 


    pg.display.update()

pg.init()
import pygame as pg

pg.init()
size = 800
done = False
player1 = [25, size/2-100]
player2 = [size-50, size/2-100]
ball = [size/2-12, size/2-12, 270]
clock = pg.time.Clock()
pg.display.set_caption('Pong') 
screen = pg.display.set_mode((size, size))
pressed_up = False
pressed_down = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        if event.type == pg.KEYDOWN:                   
            if event.key == pg.K_w:        
                pressed_up = True
            elif event.key == pg.K_s:    
                pressed_down = True

        if event.type == pg.KEYUP:           
            if event.key == pg.K_w:        
                pressed_up = False
            elif event.key == pg.K_s:   
                pressed_down = False   

    if pressed_up:
        player1[1] -= 5
    if pressed_down:
        player1[1] += 5 

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255,255,255), (player1[0], player1[1], 25, 200))
    pg.draw.rect(screen, (255,255,255), (player2[0], player2[1], 25, 200))

    pg.draw.rect(screen, (255,255,255), (ball[0], ball[1], 25, 25))
    pg.display.update()
    clock.tick(30)
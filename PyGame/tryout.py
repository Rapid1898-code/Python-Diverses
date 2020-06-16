import sys
import pygame as pg

def run_game():

    pg.init()
    screen_dim = (1200,800)
    screen = pg.display.set_mode(screen_dim)
    pg.display.set_caption("PyGame")
    bg_color = (230,230,230)
    screen.fill(bg_color)
    screen_rect = screen.get_rect()
    bullet_rect = pg.Rect(100,100,10,150)
    color = (100,100,100)
    pg.draw.rect(screen,color,bullet_rect)
    ship = pg.image.load("ship.png")
    ship_rect = ship.get_rect()
    ship_rect.midbottom = screen_rect.midbottom
    screen.blit(ship,ship_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pg.display.flip()

run_game()

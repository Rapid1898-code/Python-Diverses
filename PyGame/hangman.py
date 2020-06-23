import pygame as pg
import os

# setup display
pg.init()
WIDTH,HEIGHT = 800,500
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Hangman Game")

# load images
images = []
for i in range(6):
    pg.image.load("hangman0.png")
    # image = pg.image.load("hangman" + str(i) + ".png")
    images.append()
print(images)

# setup game loop
FPS = 60
clock = pg.time.Clock()
run = True

while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            print(pos)

pg.quit()






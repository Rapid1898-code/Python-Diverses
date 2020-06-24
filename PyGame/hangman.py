import pygame as pg
import os
from sys import platform

# setup display
pg.init()
WIDTH,HEIGHT = 800,500
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Hangman Game")

# fonts
LETTER_FONT = pg.font.SysFont("comicsans",40)

# load images
images = []
for i in range(6):
    if platform == "win32": image = pg.image.load("hangman" + str(i) + ".png")
    elif platform == "linux": image = pg.image.load("/home/rapid1898/Dokumente/GitHub/Python-Diverses/PyGame/hangman" + str(i) + ".png")
    images.append(image)

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS *2))
    letters.append([x,y,chr(A + i)])

# game variables
hangman_status = 0

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup game loop
FPS = 60
clock = pg.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw buttons
    for letter in letters:
        x,y,ltr = letter
        pg.draw.circle(win,BLACK,(x,y),RADIUS,3)
        text = LETTER_FONT.render(ltr,1,BLACK)
        win.blit(text,(x - text.get_width()/2,y - text.get_height()/2))

    win.blit(images[hangman_status], (150,100))
    pg.display.update()

while run:
    clock.tick(FPS)

    draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            print(pos)

pg.quit()






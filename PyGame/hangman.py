import pygame as pg
import os
from sys import platform
import math
import random

# setup display
pg.init()
WIDTH,HEIGHT = 800,500
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Hangman Game")

# fonts
LETTER_FONT = pg.font.SysFont("comicsans",40)
WORD_FONT = pg.font.SysFont("comicsans",60)
TITLE_FONT = pg.font.SysFont("comicsans",70)

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
    letters.append([x,y,chr(A + i),True])

# game variables
hangman_status = 0
words = ["IDE","REPLIT","PYTHON","PYGAGME"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup game loop
FPS = 60
clock = pg.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    # draw titlle
    text = TITLE_FONT.render("DEVELOPER HANGMAN",1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text,(400,200))

    # draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pg.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x - text.get_width()/2,y - text.get_height()/2+1))

    win.blit(images[hangman_status], (150,100))
    pg.display.update()

def display_message(message):
    pg.time.delay(1000)
    win.fill (WHITE)
    text = WORD_FONT.render (message, 1, BLACK)
    win.blit (text, (WIDTH/2 - text.get_width () / 2, HEIGHT / 2 - text.get_height () / 2))
    pg.display.update ()
    pg.time.delay (3000)

while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            m_x, m_y = pg.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON!")
        break

    if hangman_status == 6:
        display_message("You LOST!")
        break

pg.quit()






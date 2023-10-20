import pygame

#size constants
WIDTH, HEIGHT = 800,800
#must be even and >= 4
ROWS = COLS = 8
SQUARE_SIZE = WIDTH//COLS

#RGB colour constants

#Pieces
WHITE = (255,255,255)
BLACK = (0,0,0)
    #outline
GREY = (128,128,128)

#checker board
LIME = (0,186,0)
GREEN = (0, 102, 0)

#AI
AI_ON = True
AI = BLACK
PLAYER = WHITE
DEPTH = 3

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
AI = WHITE
PLAYER = BLACK
DEPTH = 3
WEIGHT = [0.5,2]

    #piece square table
PIECESQUARETABLE = [
    [ 1.00, -0.25,  0.10,  0.05,  0.05,  0.10, -0.25,  1.00],
    [-0.25, -0.25,  0.01,  0.01,  0.01,  0.01, -0.25, -0.25],
    [ 0.10,  0.01,  0.05,  0.02,  0.02,  0.05,  0.01,  0.10],
    [ 0.05,  0.01,  0.02,  0.01,  0.01,  0.02,  0.01,  0.05],
    [ 0.05,  0.01,  0.02,  0.01,  0.01,  0.02,  0.01,  0.05],
    [ 0.10,  0.01,  0.05,  0.02,  0.02,  0.05,  0.01,  0.10],
    [-0.25, -0.25,  0.01,  0.01,  0.01,  0.01, -0.25, -0.25],
    [ 1.00, -0.25,  0.10,  0.05,  0.05,  0.10, -0.25,  1.00],
]

#setup position

SETUP_ON = False

SETUP = [
    [WHITE,WHITE,WHITE,  0  ,WHITE,WHITE,WHITE,WHITE],
    [BLACK,WHITE,WHITE,BLACK,BLACK,BLACK,BLACK,BLACK],
    [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK],
    [WHITE,WHITE,BLACK,WHITE,WHITE,BLACK,WHITE,BLACK],
    [WHITE,WHITE,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK],
    [WHITE,BLACK,WHITE,BLACK,WHITE,  0  ,BLACK,BLACK],
    [WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK],
    [WHITE,  0  ,WHITE,BLACK,BLACK,BLACK,BLACK,WHITE]
]

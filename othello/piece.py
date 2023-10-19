from .constants import SQUARE_SIZE, GREY
import pygame

class Piece:
    #PADDING determines piece size bidder padding means smaller piece
    PADDING = 15
    OUTLINE = 2

    def __init__(self,row,col,colour):
        self.row = row
        self.col = col
        self.colour = colour

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x =  SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y =  SQUARE_SIZE*self.row + SQUARE_SIZE//2
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius+self.OUTLINE)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)

    def set_colour(self, colour):
        self.colour = colour

    def __repr__(self):
        return "({},{})".format(self.row,self.col)
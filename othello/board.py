import pygame
from .constants import BROWN, ROWS, BEIGE, SQUARE_SIZE, COLS, BLACK, RED
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.red_left = 12
        self.black_kings = self.red_kings = 0

        #runs the create_board function on start up to set pieces
        self.create_board()

    def draw_squares(self,win):
        #background colour
        win.fill(BROWN)
        #adding Beige squares in checker board pattern
        for row in range (ROWS):
            #row%2 determines if first square is missed out or not
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == ROWS-1 or row==0:
            piece.make_king()
            if piece.king == False:
                if piece.colour == BLACK:
                    self.black_kings +=1
                else:
                    self.red_kings +=1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        pass

    def draw(self,win):
        #draws squares and pieces
        self.draw_squares(win)
        

    
    def remove(self,pieces):
        for piece in pieces:
            self.board[piece.row][piece.col]=0
            if piece!= 0:
                if piece.colour ==RED:
                    self.red_left -=1
                else:
                    self.black_left -=1

    def winner(self):
        if self.red_left<=0:
            return BLACK
        elif self.black_left<=0:
            return RED
        else:
            return None

    def get_valid_moves(self, piece):
        pass

    def _traverse_left(self, start, stop, step, colour, left, skipped = []):
        pass
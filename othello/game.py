import pygame
from .constants import WHITE, BLACK, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.notTurn = WHITE
        self.valid_moves = self.board.get_valid_moves(self.turn, self.notTurn)

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self,row,col):
        for moves in self.board.get_valid_moves(self.turn, self.notTurn):
            if row == moves[0] and col == moves[1]:
                self.board.turn(row,col,self.turn, self.notTurn)
        self.update()

    def draw_valid_moves(self, moves):
        for move in moves:
            row=move[0]
            col=move[1]
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves={}
        #swaps turns
        if self.turn == WHITE:
            self.turn = BLACK
            self.notTurn = WHITE
        else:
            self.turn = WHITE
            self.notTurn = BLACK

    
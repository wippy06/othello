import pygame
from .constants import WHITE, BLACK, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.valid_moves = self.board.get_valid_moves(self.turn, self.notTurn)
        self.draw_valid_moves(self.valid_moves,self.turn)
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
                self.change_turn()
                if self.board.get_valid_moves(self.turn,self.notTurn)==[]:
                    self.change_turn()
                    return True
                break
        

    def draw_valid_moves(self, moves,colour):
        radius = (SQUARE_SIZE//2)*0.30
        for move in moves:
            row,col=move
            pygame.draw.circle(self.win, colour, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), radius)

    def change_turn(self):
        self.valid_moves={}
        #swaps turns
        if self.turn == WHITE:
            self.turn = BLACK
            self.notTurn = WHITE
        else:
            self.turn = WHITE
            self.notTurn = BLACK

    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        if self.board.board != board.board:
            self.board = board
            self.change_turn()
            if self.board.get_valid_moves(self.turn,self.notTurn)==[]:
                self.change_turn()
                return True


    
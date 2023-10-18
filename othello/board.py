import pygame
from .constants import GREEN, ROWS, LIME, SQUARE_SIZE, COLS, BLACK, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []

        #runs the create_board function on start up to set pieces
        self.create_board()

    def draw_squares(self,win):
        #background colour
        win.fill(GREEN)
        #adding LIME squares in checker board pattern
        for row in range (ROWS):
            #row%2 determines if first square is missed out or not
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(win, LIME, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def turn(self):
        pass

    def get_all_pieces(self, colour):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece!= 0 and piece.colour == colour:
                    pieces.append(piece)
        return pieces 

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):

                if (col == 3 and row == 3) or (col == 4 and row == 4):

                    self.board[row].append(Piece(row,col, WHITE))
                
                elif (col == 4 and row == 3) or (col == 3 and row == 4):

                    self.board[row].append(Piece(row,col, BLACK))


                else:
                    self.board[row].append(0)

    def draw(self,win):
        #draws squares and pieces
        self.draw_squares(win)
       #cycles through squares in the array to check if piece needs to be drawn
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    #piece is drawn if the space in the array is not 0
                    piece.draw(win)

    def winner(self):
        pass

    def get_valid_moves(self, colour, anticolour):
        moves = []
        for piece in self.get_all_pieces(colour):
            row = piece.row
            col = piece.col
            # if there is an opposite piece below the piece that is not a 0
            if self.get_piece(row+1,col) != 0 and self.get_piece(row+1,col).colour == anticolour:
                #find how many in the col below the piece
                for x in range(ROWS-(row+1)):
                    #if there is an empty space add that coordinate to a list
                    if self.get_piece(row + x +1,col) == 0:
                        moves.append((row + x +1,col))
                        break

            #same for above
            if self.get_piece(row-1,col) != 0 and self.get_piece(row-1,col).colour == anticolour:
                for x in range(ROWS-(row-1)):
                    if self.get_piece(row - x -1,col) == 0:
                        moves.append((row - x -1,col))
                        break
            
            #same for to the right
            if self.get_piece(row,col+1) != 0 and self.get_piece(row,col+1).colour == anticolour:
                for x in range(COLS-(col+1)):
                    if self.get_piece(row,col + x +1) == 0:
                        moves.append((row,col + x +1))
                        break
            
            #same for to the left
            if self.get_piece(row,col-1) != 0 and self.get_piece(row,col-1).colour == anticolour:
                for x in range(COLS-(col-1)):
                    if self.get_piece(row,col - x -1) == 0:
                        moves.append((row,col - x -1))
                        break

            #down right
            if self.get_piece(row+1,col+1) != 0 and self.get_piece(row+1,col+1).colour == anticolour:
                minimum = min(COLS-(col+1),ROWS-(row+1))
                for x in range(minimum):                   
                    if self.get_piece(row+x+1,col+x+1) == 0:
                        moves.append((row+x+1,col+x+1))
                        break
            
            #down left
            if self.get_piece(row+1,col-1) != 0 and self.get_piece(row+1,col-1).colour == anticolour:
                minimum = min(COLS-(col-1),ROWS-(row+1))
                for x in range(minimum):                   
                    if self.get_piece(row+x+1,col-x-1) == 0:
                        moves.append((row+x+1,col-x-1))
                        break

            #up right
            if self.get_piece(row-1,col+1) != 0 and self.get_piece(row-1,col+1).colour == anticolour:
                minimum = min(COLS-(col+1),ROWS-(row-1))
                for x in range(minimum):                   
                    if self.get_piece(row-x-1,col+x+1) == 0:
                        moves.append((row-x-1,col+x+1))
                        break

            #up left
            if self.get_piece(row-1,col-1) != 0 and self.get_piece(row-1,col-1).colour == anticolour:
                minimum = min(COLS-(col-1),ROWS-(row-1))
                for x in range(minimum):                   
                    if self.get_piece(row-x-1,col-x-1) == 0:
                        moves.append((row-x-1,col-x-1))
                        break

        return moves

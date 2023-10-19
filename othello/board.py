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

    def turn(self, row, col, colour, anticolour):
        self.addPiece(row, col, colour)
        pieces = self.findPieces(row, col, anticolour)
        self.flipPieces(pieces, colour)

    def addPiece(self, row,col,colour):
        self.board[row][col] = Piece(row,col, colour)

    def findPieces(self, row,col,anticolour):
        pieces = []

        area=[-1,0,1]
        for rowOffset in area:
            for colOffset in area:
                if not (rowOffset ==0 and colOffset == 0):
                    pieces = [*pieces, *(self.check_lane([row,col], [rowOffset,colOffset], anticolour, True))]

        return pieces
    

    def flipPieces(self, pieces, colour):
        for piece in pieces:
            piece.set_colour(colour)

    def check_lane(self, position, direction, oppColour, getPieces):
        moves = []
        pieces = []

        nextRow = position[0] + direction[0]
        nextCol = position[1] + direction[1]

        newPos = [nextRow, nextCol]
        
        if(nextRow > ROWS-1 or nextCol > COLS-1 or nextRow < 0 or nextCol < 0):
            return []
        
        #checks if next piece is opposite colour
        pieceColour = self.getColourAtPosition(newPos, oppColour)
        if pieceColour == -1:
            #opposite colour
            pieces = self.check_lane(newPos, direction, oppColour, getPieces)
            
            if getPieces and len(pieces) >0:
                pieces.append(self.get_piece(newPos[0], newPos[1]))    
            return pieces
        
        elif pieceColour == 1:
            #same colour as current player
            if getPieces:
                #return pieces
                return [self.get_piece(newPos[0], newPos[1])]
            
        elif pieceColour == 0 and self.getColourAtPosition(position, oppColour)== -1:
            #empty space on newPos and at posiion its same colour as opposite player
            moves.append(newPos)
            if not getPieces:
                return moves
            
        return[] 
    
    def getColourAtPosition(self, position, anticolour):
        piece = self.get_piece(position[0], position[1])
        if piece == 0:
            return 0
        elif piece.colour == anticolour:
            return -1
        else:
            return 1

    def get_valid_moves(self, colour, anticolour):
        moves = []
        for piece in self.get_all_pieces(colour):
            row = piece.row
            col = piece.col
            
            area=[-1,0,1]
            for rowOffset in area:
                for colOffset in area:
                    if not (rowOffset ==0 and colOffset == 0):
                        moves = [*moves, *(self.check_lane([row,col], [rowOffset,colOffset], anticolour, False))]

        return moves


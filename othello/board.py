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

    def turn(self, row, col, colour, anticolour):
        self.addPiece(row, col, colour)
        pieces = self.findPieces(row, col, anticolour)
        self.flipPieces(pieces)


    def addPiece(self, row,col,colour):
        self.board[row][col] = Piece(row,col, colour)

    def findPieces(self, row,col,anticolour):
        pieces = []

        #check lanes for pieces
        pieces.append(self.check_lane(row+1, col  , anticolour, ["+x","+0"], True))
        pieces.append(self.check_lane(row-1, col  , anticolour, ["-x","+0"], True))
        pieces.append(self.check_lane(row  , col+1, anticolour, ["+0","+x"], True))
        pieces.append(self.check_lane(row  , col-1, anticolour, ["+0","-x"], True))
        pieces.append(self.check_lane(row+1, col+1, anticolour, ["+x","+x"], True))
        pieces.append(self.check_lane(row+1, col-1, anticolour, ["+x","-x"], True))
        pieces.append(self.check_lane(row-1, col+1, anticolour, ["-x","+x"], True))
        pieces.append(self.check_lane(row-1, col-1, anticolour, ["-x","-x"], True))

        pieces.sort(key=self.key_by_len)

        for x in range(len(pieces)):
            if pieces[0] == []:
                pieces.pop(0)

        piece_list = []
        for x in range(len(pieces)):
            piece_list.append(pieces[x][0])
            
        return piece_list


    def flipPieces(self, pieces):
        for piece in pieces:
            piece.flip_colour()
        print(pieces)


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

                if (col == 3 and row == 3) or (col == 4 and row == 4)or (col == 4 and row == 5):

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


    def check_lane(self,row,col,anticolour,function, getPieces):
        moves = []
        pieces = []

        if self.get_piece(row,col) != 0 and self.get_piece(row,col).colour == anticolour:
                minimum = min(COLS-(col),ROWS-(row))
                for x in range(minimum):
                    if getPieces and self.get_piece(eval(str(row)+function[0]),eval(str(col)+function[1])) != 0 and self.get_piece(eval(str(row)+function[0]),eval(str(col)+function[1])).colour == anticolour:
                        piece = self.get_piece(eval(str(row)+function[0]),eval(str(col)+function[1]))
                        pieces.append(piece)      
                    if self.get_piece(eval(str(row)+function[0]),eval(str(col)+function[1])) == 0 or self.get_piece(eval(str(row)+function[0]),eval(str(col)+function[1])).colour != anticolour:
                        moves.append((int(eval(str(row)+function[0])),int(eval(str(col)+function[1]))))
                        break
        if getPieces:
            return pieces
        else:
            return moves

    def get_valid_moves(self, colour, anticolour):
        moves = []
        for piece in self.get_all_pieces(colour):
            row = piece.row
            col = piece.col
            moves.append(self.check_lane(row+1, col  , anticolour, ["+x","+0"], False))
            moves.append(self.check_lane(row-1, col  , anticolour, ["-x","+0"], False))
            moves.append(self.check_lane(row  , col+1, anticolour, ["+0","+x"], False))
            moves.append(self.check_lane(row  , col-1, anticolour, ["+0","-x"], False))
            moves.append(self.check_lane(row+1, col+1, anticolour, ["+x","+x"], False))
            moves.append(self.check_lane(row+1, col-1, anticolour, ["+x","-x"], False))
            moves.append(self.check_lane(row-1, col+1, anticolour, ["-x","+x"], False))
            moves.append(self.check_lane(row-1, col-1, anticolour, ["-x","-x"], False))

        moves.sort(key=self.key_by_len)

        for x in range(len(moves)):
            if moves[0] == []:
                moves.pop(0)

        moves_list = []
        for x in range(len(moves)):
            moves_list.append(moves[x][0])
            
        return moves_list
    
    def key_by_len(self,e):
        return len(e)


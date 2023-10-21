import pygame, random
from othello.constants import WIDTH,HEIGHT, SQUARE_SIZE, AI, DEPTH, AI_ON, WEIGHT0, WEIGHT1, AI_VS_AI
from othello.game import Game
from minimax.algorithm import minimax


FPS = 60

#set display size and capiton
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello")

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    debugSelect = False
 
    while run:
        clock.tick(FPS)

        if game.turn == AI and AI_ON:
            new_board = minimax(game.get_board(), DEPTH, True, float("-inf"), float("inf"), WEIGHT0)
            aiSelect = game.ai_move(new_board[1])
            
            if aiSelect:
                print("pass")

        game.update()

        if game.notTurn == AI and AI_VS_AI and AI_ON:
            new_board = minimax(game.get_board(), DEPTH, False, float("-inf"), float("inf"), WEIGHT1)
            aiSelect = game.ai_move(new_board[1])
            
            if aiSelect:
                print("pass")
        
        if game.winner()!=None:
            print(game.winner())

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                print(game.turn, game.valid_moves, game.board.evaluate(WEIGHT0), game.board.evaluate(WEIGHT1), game.winner(), debugSelect, game.board.board)
            
            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                select = game.select(row, col)
                debugSelect = select
                if select:
                    print("pass")


        #draws the board        
        game.update()

    pygame.quit()

#runs the main function
main()
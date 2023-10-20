import pygame
from othello.constants import WIDTH,HEIGHT, SQUARE_SIZE, AI, DEPTH, AI_ON
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

 
    while run:
        clock.tick(FPS)

        
        if game.turn == AI and AI_ON:
            new_board = minimax(game.get_board(), DEPTH, AI)
            run = game.ai_move(new_board[1])

        
        if game.winner()!=None:
            print(game.winner())

        for event in pygame.event.get():
            
            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                select = game.select(row, col)
                if select == True:
                    print("pass")


        #draws the board        
        game.update()

    pygame.quit()

#runs the main function
main()
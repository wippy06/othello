import pygame
from othello.constants import WIDTH,HEIGHT, SQUARE_SIZE, AI, DEPTH, AI_ON, AI_VS_AI, LEARN
from othello.game import Game
from minimax.algorithm import minimax
import random
import time

FPS = 60

#set display size and capiton
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello")

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def playGame(weight0, weight1):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    debugSelect = False

    game.update()

    transposisitonTableWhite = {}
    transposisitonTableBlack = {}

    clock.tick(FPS)

    plyCount = 0
 
    while run:

        if game.turn == AI and AI_ON:
            new_board = minimax(game.get_board(), DEPTH, True, float("-inf"), float("inf"), weight0, transposisitonTableBlack)
            aiSelect = game.ai_move(new_board)
            
            if aiSelect:
                print("pass")

            game.update()

            plyCount += 1

        if game.notTurn == AI and AI_VS_AI and AI_ON:
            new_board = minimax(game.get_board(), DEPTH, False, float("-inf"), float("inf"), weight1, transposisitonTableWhite)
            aiSelect = game.ai_move(new_board)
            
            if aiSelect:
                print("pass")

            game.update()
            
            plyCount += 1
        
        if game.winner()!=None:
            print(game.winner())
            run = False
            return [game.winner(), plyCount]

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                print(game.turn, game.valid_moves, game.board.evaluate(weight0), game.board.evaluate(weight1), game.winner(), debugSelect, game.board.board)
            
            #checks if game is shut down
            if event.type == pygame.QUIT:
                run = False
                return "end"
            
            #checks is mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                select = game.select(row, col)
                debugSelect = select
                print(select)
                if select:
                    print("pass")
                game.update()    

    pygame.quit()

def main():
    run = True
    change = 2
    weight0 = []
    weight1 = []
    game_count = 0

    open('othelloResults.txt', 'w').close()
    train_start = time.perf_counter()

    while run == True:
        file = open("othelloResults.txt", "a")
        if change == 2:
            weight0 = [random.randint(1,100),random.randint(1,100)]
            weight1 = [random.randint(1,100),random.randint(1,100)]
        elif change == 1:
            weight1 = [random.randint(1,100),random.randint(1,100)]
        else:
            weight0 = [random.randint(1,100),random.randint(1,100)]

        time_start = time.perf_counter()
        result = playGame(weight0, weight1)
        time_end = time.perf_counter()
        time_diff = round(time_end-time_start) 

        if result=="end":
            train_end = time.perf_counter()
            train_time = round(train_end-train_start) 
            file.write("end.{}.{}".format(train_time, game_count))
            run = False
        elif result[0] == "black wins":
            game_count +=1
            change = 0
        elif result[0] == "white wins":
            game_count +=1
            change = 1
        else:
            game_count +=1
            change = 2

        if run ==True:
            resultString = "{}.{}.{}.{}.{}\n".format(result[0], weight0, weight1, time_diff, result[1])
            file.write(resultString)
        file.close()    
    print("end.{}.{}".format(train_time, game_count))       

if LEARN == True:
    main()
else:
    playGame([6,7], [6,7])

from copy import deepcopy
import fen, art, engine, pieces
from board import Board
from engine import Engine
import time


def main():
    #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1' #start FEN string
    FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    board = fen.Translator(FEN).board
    game = Board(board)
    w_time, b_time = 60000, 60000 #time is given in milliseconds

    nyx = Engine(False, 3, b_time)
    kyrios = Engine(True, 3, w_time)
    

    game.draw_board()
    print("\n")
    print("--- START ---".center(33))
    game.draw_board()
    print("\n\n")
    print("\n")
    for i in range(1, 52):
        print(f"--- MOVE {i} ---".center(33))
        for bot in kyrios, nyx:
            bot.find_best_move(game)
        
        game.draw_board()
        #game.check_game_over()
        w_move, b_move = kyrios.index_to_algebraic(kyrios.best_move), nyx.index_to_algebraic(nyx.best_move)
        print(f"W: {w_move}\t\t\t B: {b_move}")
        print(f"W:{kyrios.time_left / 1000 : .2f}\t\t B:{nyx.time_left / 1000 : .2f}")
        game.update_pgn(f'{i}. {w_move} {b_move} ')
        print("\n\n")

if __name__ == '__main__':
    main()
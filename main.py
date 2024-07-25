
from copy import deepcopy
import fen, art, engine, pieces
from board import Board
from engine import Engine
import time


def main():
    #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    board = fen.Translator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1').board
    game = Board(board)
    
    nyx = Engine(False, 1)
    kyrios = Engine(True, 4)
    
    game.draw_board()
    for i in range(1, 10):
        print("MOVE", i)
        kyrios.find_best_move(game)
        nyx.find_best_move(game)
        game.draw_board()
        print("\n\n")
 
if __name__ == '__main__':
    main()
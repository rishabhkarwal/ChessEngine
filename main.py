from curses.ascii import isalpha

from yaml import KeyToken
import fen, art, engine, pieces
from board import Board
import time


def main():
    board = fen.Translator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1').board
    kyrios = engine.Engine(board)
    
    for i, square in enumerate(kyrios.board):
        if isalpha(square):
            kyrios.board[i] = pieces.Piece(i, square)

    kyrios.draw_board()
    print()
    print(kyrios.evaluate_board())

    one = kyrios.try_move("e2e3")
    #kyrios.draw_board()
    #kyrios.draw_board(one)

if __name__ == '__main__':
    main()
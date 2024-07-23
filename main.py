from curses.ascii import isalpha
import fen, art, engine, pieces
from board import Board
import time


def main():
    #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    board = fen.Translator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1').board
    kyrios = engine.Engine(board)
    
    for i, square in enumerate(kyrios.board):
        if isalpha(square):
            kyrios.board[i] = pieces.Piece.assign_piece(i, square)

    kyrios.draw_board(kyrios.board)
    print()
    kyrios.search_moves(1, kyrios.board, True)
    #kyrios.evaluate_board()

    #one = kyrios.try_move("e2e3")
    #kyrios.draw_board()
    #two = kyrios.index_to_algebraic([52, 36])
    #print(two)
    #three = kyrios.algebraic_to_index("e2e4")
    #print(three)
    #kyrios.draw_board(one)

if __name__ == '__main__':
    main()
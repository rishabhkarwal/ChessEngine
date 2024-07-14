import fen, art, engine, pieces
from board import Board
import time


def main():
    board = fen.Translator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1').board
    abcd = engine.Engine(board)
    abcd.draw_board()
    print() 
    #squares : list[str] = [f'{file}{rank}' for rank in '12345678' for file in 'abcdefgh']
    #print(list(zip(squares, board)))
    abcd.make_move("e2e3")
    abcd.draw_board()
if __name__ == '__main__':
    main()
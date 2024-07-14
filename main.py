import fen, art, engine, pieces
from board import Board
import time


def main():
    misc = engine.Engine()
    brd = fen.Translator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    brd = brd.board
    misc.generate(brd)

    board = art.draw(list(brd.values())) 
    print(brd)
    print(board)
    misc.draw()

    startTime = time.time()

        
if __name__ == "__main__":
    main()
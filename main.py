import fen, art, engine, time

def main():
    startTime = time.time()
    misc = engine.Engine()
    board = fen.Translator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print(board.board)
    board = art.draw(list(board.board.values())) 
    misc.generate(board)
    #misc.draw()

    print(round(time.time()-startTime, 2), end='\r')

    
if __name__ == "__main__":
    main()
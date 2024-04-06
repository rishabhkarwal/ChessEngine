import fen, art, engine, pieces
from board import Board
import pygame, time

pygame.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
clock = pygame.time.Clock()

def main():
    #misc = engine.Engine()
    brd = fen.Translator("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    brd = brd.board
    #board = art.draw(list(board.board.values())) 
    #print(brd)
    board = Board(squareSize=HEIGHT//8, boardInfo=brd)
    #misc.draw()
    startTime = time.time()

    while 1:
        screen.fill("black")
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()
        board.displayBoard(screen)

        mouse = pygame.mouse.get_pos()
        for square in board.squares:
            if square.rect.collidepoint(mouse):
                pygame.draw.rect(screen, (255, 255, 220), square.rect, 1)
                print(square.piece)
        
        pygame.display.set_caption(f"FPS: {str(int(clock.get_fps()))}  ¦  Time: {round(time.time() - startTime, 2)}") 
        pygame.display.update()
        
if __name__ == "__main__":
    main()
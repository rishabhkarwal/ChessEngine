import pygame
import pygame.freetype

class Board:
    def __init__(self, squareSize, boardInfo, lightColour = (188, 161, 125), darkColour = (106, 74, 49)):
        self.squareSize = squareSize
        self.lightColour = lightColour
        self.darkColour = darkColour
        self.boardInfo = boardInfo
        self.squares = self.generateSquares()
        

    def generateSquares(self):
        piecesArt = {"B":{True:"♝", False:"♗"}, "K":{True:"♚", False:"♔"},
                    "N":{True:"♞", False:"♘"}, "P":{True:"♟", False:"♙"}, 
                    "Q":{True:"♛", False:"♕"}, "R":{True:"♜", False:"♖"}}
        squares = []
        squareIndex = 0
        for f in range(0, 8): #file (vertical)
            for r in range(0, 8): #rank (horizontal)
                isLight = ((f + r) % 2 == 0)
                squareColour = self.lightColour if isLight else self.darkColour

                squareRect = pygame.Rect(int(self.squareSize*r), int(self.squareSize*f), self.squareSize, self.squareSize)
                art = piecesArt[self.boardInfo[squareIndex].capitalize()][self.boardInfo[squareIndex].isupper()] if self.boardInfo[squareIndex] != None else " "
                squares += [self.Square(squareIndex, self.boardInfo[squareIndex], art, squareRect, squareColour)]
                squareIndex += 1
        return squares
    
    def displayBoard(self, surface):
        font = pygame.font.SysFont("Consolas", 40)
        for square in self.squares:
            pygame.draw.rect(surface, square.colour, square.rect)
            text = font.render(square.piece, True, (253, 246, 210))
            surface.blit(text, text.get_rect(center = square.rect.center))

    class Square:
        def __init__(self, index, piece, art, rect, colour):
            self.index = index
            self.piece = piece
            self.art = art
            self.rect = rect
            self.colour = colour
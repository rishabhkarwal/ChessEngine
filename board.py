

class Board:
    def __init__(self, squareSize, boardInfo, lightColour = (188, 161, 125), darkColour = (106, 74, 49)):
        self.squareSize = squareSize
        self.lightColour = lightColour
        self.darkColour = darkColour
        self.boardInfo = boardInfo
        self.squares = self.generateSquares()
        
    class Square:
        def __init__(self, index, piece, art, rect, colour):
            self.index = index
            self.piece = piece
            self.art = art
            self.rect = rect
            self.colour = colour
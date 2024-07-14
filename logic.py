import time

class Game:
    def __init__(self):
        self.white = self.Player("white", [1])
        self.black = self.Player("black", [0])

    def evaluate(self):
        pass

    class Player:
        def __init__(self, colour, pieces):
            self.colour = colour
            self.pieces = pieces
            self.timer = time.time()-time.time()
        
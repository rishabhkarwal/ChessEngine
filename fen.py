class Translator:
    def __init__(self, fenString):
        self.fenString = fenString
        self.ranks = self.splitFen(fenString)
        self.board = self.createBoard()

    def splitFen(self, fenString):
        ranks = fenString.split("/")
        rankEight, playerTurn, castlingAvailability, enPassantTargetSquare, halfMoveClock, fullMoveCount = ranks[-1].split()
        ranks[7] = rankEight
        
        return ranks
    
    def createBoard(self, fill=" "):
        fenBoard = []
        for rank in self.ranks:
            fenBoard.append([*rank])

        board = [fill for _ in range(64)]
        index = 0
        for rank in fenBoard:
            for square in rank:
                if square.isnumeric():
                    index += int(square)
                
                if square.isalpha():
                    board[index] = str(square)
                    index += 1
        return board
    


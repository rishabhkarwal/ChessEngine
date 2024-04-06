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
    
    def createBoard(self):
        fenBoard = []
        for rank in self.ranks:
            fenBoard.append([*rank])
        
        board = {i:None for i in range(64)}
        index = 0
        for rank in fenBoard:
            for square in rank:
                if square.isnumeric():
                    index += int(square)
                
                elif square.isalpha():
                    board[index] = str(square)
                    index += 1

        return board
    
    def writeBoard(self):
        for rank in self.board:
            print(rank)


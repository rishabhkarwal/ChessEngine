#board = [
#     0,  1,  2,  3,  4,  5,  6,  7,
#     8,  9, 10, 11, 12, 13, 14, 15,
#    16, 17, 18, 19, 20, 21, 22, 23,
#    24, 25, 26, 27, 28, 29, 30, 31,
#    32, 33, 34, 35, 36, 37, 38, 39,
#    40, 41, 42, 43, 44, 45, 46, 47,
#    48, 49, 50, 51, 52, 53, 54, 55,
#    56, 57, 58, 59, 60, 61, 62, 63
#]

board = {0: 'r', 1: 'n', 2: 'b', 3: 'q', 4: 'k', 5: 'b', 6: 'n', 7: 'r', 8: 'p', 9: 'p', 10: 'p', 11: 'p', 12: 'p', 13: 'p', 14: 'p', 15: 'p', 16: None, 17: None, 18: None, 19: None, 20: None, 21: None, 22: None, 23: None, 24: None, 25: None, 26: None, 27: None, 28: None, 29: None, 30: None, 31: None, 32: None, 33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 48: 'P', 49: 'P', 50: 'P', 51: 'P', 52: 'P', 53: 'P', 54: 'P', 55: 'P', 56: 'R', 57: 'N', 58: 'B', 59: 'Q', 60: 'K', 61: 'B', 62: 'N', 63: 'R'}

class Moves:
    @staticmethod
    def getStraightMoves(index, colour):
        possible : list[int] = []
        for i in range(index + 1, (index // 8 + 1) * 8): #to the right
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 1, ((index // 8 ) * 8) - 1, -1): #to the left
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 8, -1, -8): #up
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index + 8, 64, +8): #dowm
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        return possible
    
    @staticmethod
    def getDiagonalMoves(index, colour):
        possible : list[int] = []
        for i in range(index + 9, 64, 9): #to the right down
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 7, -1, -7): #to the right up
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index + 7, 64, 7): #left down
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break

            if (i - 7) % 8 == 0:
                break

            possible += [i]

        for i in range(index - 9, -1, -9): #left up
            if board[i]:
                if board[i].isupper() != colour: #if diff colours
                    possible += [i]
                break
            possible += [i]

        return possible
    
    @staticmethod
    def getKnightMoves(index, colour): #L-Shapes
        moves : list[int] = [+10, +17, +15, +6, -10, -17, -15, -6]
        possible : list[int] = []
        for move in moves:
            temp = index + move
            if temp > 63 and temp < 0:
                break
            if board[temp]:
                if board[temp].isupper() != colour:
                    possible += [temp]
                continue
            possible += [temp]
                
        return possible
        
    
    @staticmethod
    def getPawnMoves(): #en-Passant, 2 spaces on first move, forward move but diagonal takes
        return 0
    
    @staticmethod
    def getCastleMoves(): #
        return 0

class Queen:
    def __init__(self, index, piece):
        self.value = 0
        self.index = index
        self.isWhite = True if piece.isupper() else False

    def getMoves(self):
        return Moves.getDiagonalMoves(self.index, self.isWhite) + Moves.getStraightMoves(self.index, self.isWhite)
    
class King:
    def __init__(self, index, piece):
        self.value = 0
        self.index = index
        self.isWhite = True if piece.isupper() else False

    def getMoves(self):
        return Moves.getDiagonalMoves(self.index, self.isWhite) + Moves.getStraightMoves(self.index, self.isWhite)

test = Queen(10, "q")
#print(test.getMoves())


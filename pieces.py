from pieceSquareTables import *

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

class Moves:
    board = []
    @staticmethod
    def getStraightMoves(index):
        possible : list[int] = []
        for i in range(index + 1, (index // 8 + 1) * 8): #to the right
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 1, ((index // 8 ) * 8) - 1, -1): #to the left
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 8, -1, -8): #up
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index + 8, 64, +8): #dowm
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        return possible
    
    @staticmethod
    def getDiagonalMoves(index):
        possible : list[int] = []
        for i in range(index + 9, 64, 9): #to the right down
            if abs((i - 9) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        for i in range(index - 7, -1, -7): #to the right up
            if abs((i + 7) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    
                    possible += [i]
                break
            possible += [i]

        for i in range(index + 7, 64, 7): #left down
            if abs((i - 7) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break

            if (i - 7) % 8 == 0:
                break

            possible += [i]

        for i in range(index - 9, -1, -9): #left up
            if abs((i + 9) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            if Moves.board[i] != " ":
                if Moves.board[i].isWhite != Moves.board[index].isWhite: #if diff colours
                    possible += [i]
                break
            possible += [i]

        return possible
    
    @staticmethod
    def getKnightMoves(index): #L-Shapes
        moves : list[int] = [+10, +17, +15, +6, -10, -17, -15, -6] #all L-shapes
        possible : list[int] = []
        for move in moves:
            temp = index + move
            
            if temp > 63 or temp < 0:
                continue
            if abs(index % 8 - temp % 8) > 2: #stops pieces teleporting
                continue
            if Moves.board[temp] != " ":
                if Moves.board[temp].isWhite != Moves.board[index].isWhite:
                    possible += [temp]
                continue
            possible += [temp]
                
        return possible
        
    
    @staticmethod
    def getPawnMoves(index, isWhite, hasMoved): #en-Passant, 2 spaces on first move, forward move but diagonal takes
        moves : list[int] = [-8, -16] if isWhite else [+8, +16]
        moves = moves[:1] if hasMoved else moves
        takes : list[int] = [-7, -9] if isWhite else [+7, +9]
        possible : list[int] = []
        for move in moves + takes:
            temp = index + move
            if temp > 63 or temp < 0:
                continue
            if abs(index % 8 - temp % 8) > 1: #stops pieces teleporting
                continue
            if Moves.board[temp] != " ":
                if Moves.board[temp].isWhite != Moves.board[index].isWhite:
                    possible += [temp]
                continue
            if move in takes:
                continue
            possible += [temp]

        return possible
    
    @staticmethod
    def getCastleMoves(): #
        return 0
    
    @staticmethod
    def getKingMoves(index):
        moves : list[int] = [-8, +8, -1, +1, -7, -9, +7, +9] #up, down, left, right, up-right, up-left, down-right, down-left: 1 space
        possible : list[int] = []
        for move in moves:
            temp = index + move
            
            if temp > 63 or temp < 0:
                continue
            if abs(index % 8 - temp % 8) > 1: #stops pieces teleporting
                continue
            if Moves.board[temp] != " ":
                if Moves.board[temp].isWhite != Moves.board[index].isWhite:
                    possible += [temp]
                continue
            possible += [temp]
                
        return possible
    
class Piece:
    @staticmethod
    def assign_piece(index, symbol):
        isWhite = True if symbol.isupper() else False

        if symbol.upper() == "K":
            return King(index, isWhite)
        
        elif symbol.upper() == "Q":
            return Queen(index, isWhite)
        
        elif symbol.upper() == "R":
            return Rook(index, isWhite)
        
        elif symbol.upper() == "B":
            return Bishop(index, isWhite)
        
        elif symbol.upper() == "N":
            return Knight(index, isWhite)
        
        elif symbol.upper() == "P":
            return Pawn(index, isWhite)
        
    def __str__(self):
        return str(self.symbol)
    

class Queen: #Q
    def __init__(self, index, isWhite):
        self.value = 900 #if isWhite else -9
        self.symbol = "Q" if isWhite else "q"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_queen_table, eg_queen_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getDiagonalMoves(self.index) + Moves.getStraightMoves(self.index)
    
class King: #K
    def __init__(self, index, isWhite):
        self.value = 20000# if isWhite else -900
        self.symbol = "K" if isWhite else "k"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_king_table, eg_king_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getKingMoves(self.index)

class Rook: #R
    def __init__(self, index, isWhite) -> None:
        self.value = 500# if isWhite else -5
        self.symbol = "R" if isWhite else "r"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_rook_table, eg_rook_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getStraightMoves(self.index)
    
class Pawn: #P
    def __init__(self, index, isWhite) -> None:
        self.value = 100 #if isWhite else -1
        self.symbol = "P" if isWhite else "p"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_pawn_table, eg_pawn_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getPawnMoves(self.index, self.isWhite, True)
    
class Knight: #N
    def __init__(self, index, isWhite) -> None:
        self.value = 320# if isWhite else -3
        self.symbol = "N" if isWhite else "n"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_knight_table, eg_knight_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getKnightMoves(self.index)
    
class Bishop: #B
    def __init__(self, index, isWhite) -> None:
        self.value = 330 #if isWhite else -3
        self.symbol = "B" if isWhite else "b"
        self.index = index
        self.isWhite = isWhite
        self.mg_table, self.eg_table = mg_bishop_table, eg_bishop_table
        #if not isWhite:
            #self.mg_table, self.eg_table = self.mg_table[::-1], self.eg_table[::-1]

    def getMoves(self, board):
        Moves.board = board
        return Moves.getDiagonalMoves(self.index)


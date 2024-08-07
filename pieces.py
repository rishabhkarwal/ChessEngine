from re import M

from chess import Move
from pieceSquareTables import *
from collections import namedtuple

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

'''
Move format:
------------

The move format is in long algebraic notation.
A nullmove from the Engine to the GUI should be sent as 0000.
Examples:  e2e4, e7e5, e1g1 (white short castling), e7e8q (for promotion)
'''


MOVE = namedtuple("MOVE", ["start", "end", "weight"])
CAPTURE_MULTIPLIER = 1000


class Moves:
    board = []
    @staticmethod
    def getStraightMoves(index):
        start_square = Moves.board[index]
        possible : list[MOVE] = []

        for i in range(index + 1, (index // 8 + 1) * 8): #to the right
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        for i in range(index - 1, ((index // 8 ) * 8) - 1, -1): #to the left
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        for i in range(index - 8, -1, -8): #up
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        for i in range(index + 8, 64, +8): #dowm
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        return possible
    
    @staticmethod
    def getDiagonalMoves(index):
        start_square = Moves.board[index]
        possible : list[MOVE] = []
        
        for i in range(index + 9, 64, 9): #to the right down
            if abs((i - 9) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        for i in range(index - 7, -1, -7): #to the right up
            if abs((i + 7) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        for i in range(index + 7, 64, 7): #left down
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            
            if (i - 7) % 8 == 0:
                break

            possible += [MOVE(index, i, 0)]

        for i in range(index - 9, -1, -9): #left up
            if abs((i + 9) % 8 - i % 8) != 1: #stops pieces teleporting
                break
            end_square = Moves.board[i]
            if end_square != " ": #if the square is empty
                if end_square.is_white != start_square.is_white: #if different colours
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                break
            possible += [MOVE(index, i, 0)]

        return possible
    
    @staticmethod
    def getKnightMoves(index): #L-Shapes
        start_square = Moves.board[index]
        moves : list[int] = [+10, +17, +15, +6, -10, -17, -15, -6] #all L-shapes
        possible : list[MOVE] = []
        for move in moves:
            i = index + move
            
            if i > 63 or i < 0:
                continue
            if abs(index % 8 - i % 8) > 2: #stops pieces teleporting
                continue

            end_square = Moves.board[i]
            if end_square != " ":
                if end_square.is_white != start_square.is_white:
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                continue
            possible += [MOVE(index, i, 0)]
                
        return possible
        
    
    @staticmethod
    def getPawnMoves(index, is_white, hasMoved): #en-Passant needs to be added
        start_square = Moves.board[index]
        moves : list[int] = [-8, -16] if is_white else [+8, +16]
        moves = moves[:1] if hasMoved else moves
        takes : list[int] = [-7, -9] if is_white else [+7, +9]
        possible : list[MOVE] = []
        for move in moves + takes:
            i = index + move
            
            if i > 63 or i < 0:
                continue
            if abs(index % 8 - i % 8) > 1: #stops pieces teleporting
                continue

            end_square = Moves.board[i]

            if move in takes and end_square != " ":
                if end_square.is_white != start_square.is_white:
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
            
            elif move in moves and end_square == " ":
                possible += [MOVE(index, i, 0)]

        return possible
    
    @staticmethod
    def getCastleMoves(): #
        return 0
    
    @staticmethod
    def getKingMoves(index):
        start_square = Moves.board[index]
        moves : list[int] = [-8, +8, -1, +1, -7, -9, +7, +9] #up, down, left, right, up-right, up-left, down-right, down-left: 1 space
        possible : list[MOVE] = []
        for move in moves:
            i = index + move
        
            if i > 63 or i < 0:
                continue
            if abs(index % 8 - i % 8) > 1: #stops pieces teleporting
                continue

            end_square = Moves.board[i]
            if end_square != " ":
                if end_square.is_white != start_square.is_white:
                    possible += [MOVE(index, i, end_square.value * CAPTURE_MULTIPLIER)]
                continue
            possible += [MOVE(index, i, 0)]
                
        return possible
    
class Piece:
    @staticmethod
    def assign_piece(index, symbol):
        is_white = True if symbol.isupper() else False

        if symbol.upper() == "K":
            return King(index, is_white)
        
        elif symbol.upper() == "Q":
            return Queen(index, is_white)
        
        elif symbol.upper() == "R":
            return Rook(index, is_white)
        
        elif symbol.upper() == "B":
            return Bishop(index, is_white)
        
        elif symbol.upper() == "N":
            return Knight(index, is_white)
        
        elif symbol.upper() == "P":
            return Pawn(index, is_white)
        
    def __str__(self):
        return str(self.symbol)
    

class Queen: #Q
    def __init__(self, index, is_white):
        self.value = 9 #900
        self.symbol = "Q" if is_white else "q"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_queen_table, eg_queen_table
        
    def get_moves(self, board):
        Moves.board = board
        return Moves.getDiagonalMoves(self.index) + Moves.getStraightMoves(self.index)
    
class King: #K
    def __init__(self, index, is_white):
        self.value = 20000 #20000
        self.symbol = "K" if is_white else "k"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_king_table, eg_king_table
        

    def get_moves(self, board):
        Moves.board = board
        return Moves.getKingMoves(self.index)

class Rook: #R
    def __init__(self, index, is_white) -> None:
        self.value = 5# 500
        self.symbol = "R" if is_white else "r"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_rook_table, eg_rook_table
        

    def get_moves(self, board):
        Moves.board = board
        return Moves.getStraightMoves(self.index)
    
class Pawn: #P
    def __init__(self, index, is_white) -> None:
        self.value = 1 #100
        self.symbol = "P" if is_white else "p"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_pawn_table, eg_pawn_table
        self.startRank = 6 if is_white else 1

    def get_moves(self, board):
        Moves.board = board
        hasMoved = True if self.index // 8 != self.startRank else False
        return Moves.getPawnMoves(self.index, self.is_white, hasMoved)
    
class Knight: #N
    def __init__(self, index, is_white) -> None:
        self.value = 3 #320
        self.symbol = "N" if is_white else "n"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_knight_table, eg_knight_table
        

    def get_moves(self, board):
        Moves.board = board
        return Moves.getKnightMoves(self.index)
    
class Bishop: #B
    def __init__(self, index, is_white) -> None:
        self.value = 3 #330
        self.symbol = "B" if is_white else "b"
        self.index = index
        self.is_white = is_white
        self.mg_table, self.eg_table = mg_bishop_table, eg_bishop_table
        

    def get_moves(self, board):
        Moves.board = board
        return Moves.getDiagonalMoves(self.index)


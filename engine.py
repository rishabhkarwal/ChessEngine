
from copy import deepcopy
import board
from pieceSquareTables import flip
from collections import namedtuple

#Piece = namedtuple("Piece", ["index", "piece"])

class Engine:
    def __init__(self, board):
        self.board = board
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}
        self.best_moves = []

    def draw_board(self, board): #arg is board
        board = [piece.symbol if type(piece) != str else " " for piece in board]
        rows = [board[x : x + 8] for x in range(0, len(board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def algebraic_to_index(self, move): #algebraic -> indexes; must be in standard notation; "e2e4", "Qh6g7+"
        return [self.chart[ele] for ele in [move[i - 1 : i + 1] for i, char in enumerate(move) if char in '12345678']]
    
    def index_to_algebraic(self, move):
        return "".join("abcdefgh"[index % 8] + "87654321"[index // 8] for index in move)
    
    def get_legal_moves(self, isWhite, board):
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        pieces = [piece for piece in pieces if piece[1].isWhite] if isWhite else [piece for piece in pieces if not piece[1].isWhite]
        moves = []
        for index, piece in pieces:
            piece.index = index
            for move in piece.get_moves(board):
                moves += [self.index_to_algebraic([piece.index, move])]
        return moves   
    
    def update_pieces(self, board):
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        for index, piece in pieces:
            piece.index = index

    def find_best_move(self, depth, board, isWhite): 
        score = self.negamax(depth, board, 1 if isWhite else -1)
        #score = self.search(depth, isWhite, -float("inf"), float("inf"))
        #self.draw_board(self.make_move(board, best_move)[1])
        print(score)
        print(best_move)

    def negamax(self, depth, board, turnMultiplier):
        global best_move
        if depth == 0:
            return turnMultiplier * self.evaluate_board(board)
        max_score = -float("inf")
        validMoves = self.get_legal_moves(isWhite=True if turnMultiplier == 1 else False, board=board)
        for move in validMoves:
            old, new = self.make_move(board, move)
            self.board = new
            self.update_pieces(self.board)
            score = -self.negamax(depth - 1, self.board, -turnMultiplier)
            self.board = old
            self.update_pieces(self.board)
            if score > max_score:
                max_score = score
                best_move = move
        return max_score

    def search(self, depth, isWhite, alpha, beta):
        global best_move
        if depth == 0:
            return self.evaluate_board(self.board)

        for move in self.get_legal_moves(isWhite, self.board):
            old, new = self.make_move(self.board, move)
            self.board = new
            self.update_pieces(self.board)
            score = -self.search(depth - 1, (not isWhite), -beta, -alpha)
            self.board = old
            self.update_pieces(self.board)
            if score >= beta:
                return beta #snip, #move was too good, opponent will avoid
            if score > alpha:
                alpha = score
                best_move = move
        return alpha

    def evaluate_board(self, board): #returns for white
        #board = args[0] if len(args) == 1 else self.board.copy()
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        w_score, b_score = 0, 0
        for piece in pieces:
            if piece[1].isWhite: w_score += piece[1].value * piece[1].mg_table[piece[0]]
            else: b_score += piece[1].value * piece[1].mg_table[flip[piece[0]]]
            #print(piece.symbol, piece.isWhite, w_score, b_score)
        return w_score - b_score

    def make_move(self, brd, move): 
        board = deepcopy(brd)
        start, end = self.algebraic_to_index(move)
        board[end] = board[start]
        board[start] = ' '
        return brd, board
    

        
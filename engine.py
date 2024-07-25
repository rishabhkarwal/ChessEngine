from curses.ascii import isalpha
from copy import deepcopy
from board import Board
import pieces
from pieceSquareTables import flip
from collections import namedtuple

#Piece = namedtuple("Piece", ["index", "piece"])

class Engine:
    def __init__(self, is_white, max_search_depth):
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}
        self.best_move = "abc"
        self.current_player = is_white #True if it's white's turn, False for black
        self.max_depth = max_search_depth

    def algebraic_to_index(self, move): #algebraic -> indexes; must be in standard notation; "e2e4", "Qh6g7+"
        return [self.chart[ele] for ele in [move[i - 1 : i + 1] for i, char in enumerate(move) if char in '12345678']]
    
    def index_to_algebraic(self, move):
        return "".join("abcdefgh"[index % 8] + "87654321"[index // 8] for index in move)
    
    def get_legal_moves(self, is_white, board):
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        pieces = [piece for piece in pieces if piece[1].is_white] if is_white else [piece for piece in pieces if not piece[1].is_white]
        moves = []
        for index, piece in pieces:
            piece.index = index
            for move in piece.get_moves(board):
                moves += [self.index_to_algebraic([piece.index, move])]
        return moves   
    
    def find_best_move(self, board): 
        depth = self.max_depth
        score = self.negamax(depth, 1 if self.current_player else -1, float('-inf'), float('inf'), board)
        board.update_board(self.make_move(board.board, self.best_move)[1])
        #return self.make_move(board.board, self.best_move)[1]
    
    def negamax(self, depth : int, color : int, alpha : float, beta : float, board : Board):
        if depth == 0:
            evaluation = color * board.evaluate_board()
            return evaluation
        
        legal_moves = self.get_legal_moves(color == 1, board.board)
        best_score = float('-inf')

        for move in legal_moves:
            old_board, new_board = self.make_move(board.board, move)
            
            board.update_board(new_board)

            score = -self.negamax(depth - 1, -color, -beta, -alpha, board)

            board.update_board(old_board)

            if score > best_score:
                best_score = score
                if depth == self.max_depth:
                    self.best_move = move

            alpha = max(alpha, score)
            if alpha >= beta: 
                break
        return best_score

    def make_move(self, initial_board, move):
        board = deepcopy(initial_board)
        start, end = self.algebraic_to_index(move)
        board[end] = board[start]
        board[start] = ' '
        return initial_board, board
from ast import Tuple
from curses.ascii import isalpha
from copy import deepcopy
from board import Board
from pieces import MOVE
from pieceSquareTables import flip
from collections import namedtuple
from random import shuffle
import time

#Piece = namedtuple("Piece", ["index", "piece"])

class Engine:
    def __init__(self, is_white, max_search_depth, time) -> None:
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}
        self.best_move = "abc"
        self.current_player = is_white #True if it's white's turn, False for black
        self.max_depth = max_search_depth
        self.time_left = time

    
    def index_to_algebraic(self, move) -> str:
        return "".join("abcdefgh"[index % 8] + "87654321"[index // 8] for index in [move.start, move.end])
    
    def get_legal_moves(self, is_white, board) -> list[MOVE]:
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        pieces = [piece for piece in pieces if piece[1].is_white] if is_white else [piece for piece in pieces if not piece[1].is_white]
        moves = []
        for index, piece in pieces:
            piece.index = index
            for move in piece.get_moves(board):
                moves += [move]
        shuffle(moves)
        return moves
    
    def find_best_move(self, board) -> None: 
        start_time = time.time_ns() 
        depth = self.max_depth
        score = self.negamax(depth, 1 if self.current_player else -1, float('-inf'), float('inf'), board)
        board.update_board(self.make_move(board.board, self.best_move)[1])
        self.time_left -= (time.time_ns() - start_time) // 1_000_000
        #return self.make_move(board.board, self.best_move)[1]
    
    def negamax(self, depth : int, colour : int, alpha : float, beta : float, board : Board) -> int:
        if depth == 0:
            return colour * board.evaluate_board()
        
        legal_moves = self.get_legal_moves(colour == 1, board.board)

        best_score = float('-inf')

        for move in legal_moves:
            old_board, new_board, weight = self.make_move(board.board, move)
            
            board.update_board(new_board)

            score = -(self.negamax(depth - 1, -colour, -beta, -alpha, board) + colour * weight) 

            board.update_board(old_board)

            if score > best_score:
                best_score = score
                if depth == self.max_depth:
                    self.best_move = move

            alpha = max(alpha, score)
            if alpha >= beta: 
                break
        return best_score

    def make_move(self, initial_board, move) -> tuple[list, list, int]:
        board = deepcopy(initial_board)
        board[move.end] = board[move.start]
        board[move.start] = ' '
        return initial_board, board, move.weight
    
    def check_end_condition(self, board):
        pass
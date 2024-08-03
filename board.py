from copy import deepcopy
import pieces
from pieceSquareTables import flip

class Board:
    def __init__(self, board):
        self.board = self.initialise_board(board)
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}
        self.pieces_art = {'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
                  'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙', ' ': '·'}
        self.initialise_pgn() 
        '''
        https://www.chess.com/analysis?tab=analysis
        https://www.apronus.com/chess/pgnviewer/
        '''

    def draw_board(self, size = 3, empty_square = "·"): #arg is board
        board = [self.pieces_art[piece.symbol] if type(piece) != str else empty_square for piece in self.board]
        rows = [board[x : x + 8] for x in range(0, len(self.board), 8)]
        [print(8 - i, (size * " ").join(row)) for i, row in enumerate(rows)]
        print(" ", (size * " ").join("abcdefgh"))

    def update_board(self, board):
        self.board = board
        self.update_pieces()

    def initialise_board(self, board):
        brd = deepcopy(board)
        for i, square in enumerate(board):
            if square != " ":
                brd[i] = pieces.Piece.assign_piece(i, square)
        return brd
    
    def update_pieces(self):
        pieces = [[i, square] for i, square in enumerate(self.board) if type(square) != str]
        for index, piece in pieces:
            piece.index = index

    def evaluate_board(self): #returns for white
        pieces = [[i, square] for i, square in enumerate(self.board) if type(square) != str]
        w_score, b_score = 0, 0
        for piece in pieces:
            if piece[1].is_white: w_score += piece[1].value * piece[1].mg_table[piece[0]]
            else: b_score += piece[1].value * piece[1].mg_table[flip[piece[0]]]
        return w_score - b_score
    
    def check_game_over(self):
        print(self.board)

    def initialise_pgn(self):
        initial = (
            '[Event "TEST"]\n'
            '[Site "TEST"]\n'
            '[Date "????.??.??"]\n'
            '[Round "?"]\n'
            '[White "BOT, Kyrios"]\n'
            '[Black "BOT, Nyx"]\n'
            '[Result "*"]\n\n'
        )
        
        with open('pgn_output.txt', 'w') as f:
            f.write(initial)



    def update_pgn(self, text):
        with open('pgn_output.txt', 'a') as f:
            f.write(text)
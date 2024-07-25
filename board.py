import pieces
from pieceSquareTables import flip

class Board:
    def __init__(self, board):
        self.board = self.initialise_board(board)
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}

    def draw_board(self): #arg is board
        board = [piece.symbol if type(piece) != str else " " for piece in self.board]
        rows = [board[x : x + 8] for x in range(0, len(self.board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def update_board(self, board):
        self.board = board
        self.update_pieces()

    def initialise_board(self, board):
        for i, square in enumerate(board):
            if square != " ":
                board[i] = pieces.Piece.assign_piece(i, square)
        return board
    
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
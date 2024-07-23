
from pieceSquareTables import flip
from collections import namedtuple

#Piece = namedtuple("Piece", ["index", "piece"])

class Engine:
    def __init__(self, board):
        self.board = board
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}

    def draw_board(self, board): #arg is board
        #board = args[0] if len(args) == 1 else self.board.copy()
        board = [piece.symbol if type(piece) != str else " " for piece in board]
        rows = [board[x : x + 8] for x in range(0, len(board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def algebraic_to_index(self, move): #algebraic -> indexes; must be in standard notation; "e2e4", "Qh6g7+"
        return [self.chart[ele] for ele in [move[i - 1 : i + 1] for i, char in enumerate(move) if char in '12345678']]
    
    def index_to_algebraic(self, move):
        return "".join("abcdefgh"[index % 8] + "87654321"[index // 8] for index in move)
    
    def getLegalMoves(self, isWhite, board):
        #board = args[0] if len(args) == 1 else self.board.copy()
        pieces = [square for square in board if type(square) != str]
        pieces = [piece for piece in pieces if piece.isWhite] if isWhite else [piece for piece in pieces if not piece.isWhite]
        moves = []
        for piece in pieces:
            for move in piece.getMoves(board):
                moves += [self.index_to_algebraic([piece.index, move])]
                #boards += [self.try_move(self.index_to_algebraic([piece.index, move]))]
        return moves   

    def search_moves(self, depth, board, isWhite, max_score=-float("inf"), best_board=[]): 
        for move in self.getLegalMoves(isWhite, board):
            brd = self.try_move(move)
            score = self.evaluate_board(brd)if isWhite else -self.evaluate_board(brd)
            print("\n")
            self.draw_board(brd)
            print(score)
            if score > max_score: max_score, best_board = score, board
        print("\n\n")
        self.draw_board(best_board)
        print(max_score)

    '''
    def negamax(self, depth, isWhite) -> int:
        if depth == 0: return evaluate()
        max = -float("inf")
        for move in self.getLegalMoves(isWhite=isWhite):
            score = -self.negamax(depth - 1,)
            if score > max: max = score
        return max
    '''

    
    def evaluate_board(self, board): #returns for white
        #board = args[0] if len(args) == 1 else self.board.copy()
        pieces = [[i, square] for i, square in enumerate(board) if type(square) != str]
        w_score, b_score = 0, 0
        for piece in pieces:
            if piece[1].isWhite: w_score += piece[1].value * piece[1].mg_table[piece[0]]
            else: b_score += piece[1].value * piece[1].mg_table[flip[piece[0]]]
            #print(piece.symbol, piece.isWhite, w_score, b_score)
        return w_score - b_score

    def try_move(self, move): 
        board = self.board.copy()
        start, end = self.algebraic_to_index(move)
        board[end] = board[start]
        board[start] = ' '
        return board
    

        
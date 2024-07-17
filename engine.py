class Engine:
    def __init__(self, board):
        self.board = board
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}

    def draw_board(self, *args): #arg is board
        board = args[0] if len(args) == 1 else self.board.copy()
        board = [piece.symbol if type(piece) != str else " " for piece in board]
        rows = [board[x : x + 8] for x in range(0, len(board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def algebraic_to_index(self, move): #algebraic -> indexes; must be in standard notation; "e2e4", "Qh6g7+"
        return [self.chart[ele] for ele in [move[i - 1 : i + 1] for i, char in enumerate(move) if char in '12345678']]
    
    def index_to_algebraic(self, move):
        return "".join("abcdefgh"[index % 8] + "87654321"[index // 8] for index in move)
    
    def evaluate_board(self, *args):
        board = args[0] if len(args) == 1 else self.board.copy()
        pieces = [square for square in board if type(square) != str]
        white = [piece for piece in pieces if piece.isWhite]
        black = [piece for piece in pieces if not piece.isWhite]
        for piece in white:
            if piece.symbol == "B":
                print(piece.symbol)
                for move in piece.getMoves(board):
                    
                    print("\n")
                    one = self.try_move(self.index_to_algebraic([piece.index, move]))
                    self.draw_board(one)
                print("\n\n\n\n\n")
        #print(white)
        #print(black)
        #print([square.index for squ5are in white])
        #print([[piece.index for piece in white if piece.symbol == p] for p in "KQRBNP"])
        #return white - black

    def try_move(self, move): 
        board = self.board.copy()
        start, end = self.algebraic_to_index(move)
        board[end] = board[start]
        board[start] = ' '
        return board
    

        
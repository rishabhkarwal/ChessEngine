class Engine:
    def __init__(self, board):
        self.board = board
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}

    def draw_board(self, *args): #arg is board
        board = args[0] if len(args) == 1 else self.board.copy()
        board = [str(ele) if type(ele) != str else " " for ele in board]
        rows = [board[x : x + 8] for x in range(0, len(board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def handle_move_input(self, move): #must be in standard notation; "e2e4", "Qh6g7+"
        res : list[str] = []
        for i, char in enumerate(move): 
            if char in '12345678':
                res += [move[i - 1 : i + 1]]
        return res
    
    def evaluate_board(self, board):
        print(board)
        
    def try_move(self, move): 
        board = self.board.copy()
        start, end = self.handle_move_input(move)
        board[self.chart[end]] = board[self.chart[start]]
        board[self.chart[start]] = ' '
        return board

        
import enum


class Engine:
    def __init__(self, board):
        self.board = board
        squares : list[str] = [f'{file}{rank}' for rank in '87654321' for file in 'abcdefgh']
        self.chart = {sq:i for i, sq in enumerate(squares)}

    def draw_board(self):
        rows = [self.board[x : x + 8] for x in range(0, len(self.board), 8)]
        [print(8 - i, row) for i, row in enumerate(rows)]
        print("   ", "    ".join(list("abcdefgh")))

    def handle_move_input(self, move): #must be in standard notation; "e2e4", "Qh6g7+"
        res : list[str] = []
        for i, char in enumerate(move): 
            if char in '12345678':
                res += [move[i - 1:i + 1]]
        return res
        
    def make_move(self, move): 
        start, end = self.handle_move_input(move)
        self.board[self.chart[end]] = self.board[self.chart[start]]
        self.board[self.chart[start]] = ' '

        

class Engine:
    def __init__(self):
        self.board = [" "]*64

    def run(self):
        print("INSERT SOMETHING NOT COOL")

    def generate(self, board):
        for piece in board:
            self.board[piece] = board[piece]

    def draw(self):
        rows = [self.board[x:x+8] for x in range(0, len(self.board), 8)]
        [print(row) for row in rows]
        
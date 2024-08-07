from fen import Translator
from board import Board
from engine import Engine

class Game:
    def __init__(self, fen : str, w_time : int, b_time : int) -> None:
        self.board = Board(Translator(fen).board)
        self.bot = Engine()
        
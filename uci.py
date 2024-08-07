class UCI:
    def __init__(self) -> None:
        pass

    @staticmethod
    def parse_position(info : str) -> tuple[str, list[str]]:
        moves = []
        first, info = info.split()[1], info.split()[2:]

        if first == "fen":
            fen_string = " ".join(info[:6])
            info = info[7:]

        elif first == "startpos":
            fen_string = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            info = info[1:]

        if len(info): moves = info

        return fen_string, moves


info = ["position fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 
        "position fen rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
        "position startpos moves e2e4", 
        "position fen rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1 moves c7c5 g1f3 d7d6"]

[UCI.parse_position(i) for i in info]
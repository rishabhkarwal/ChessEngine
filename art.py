def draw(board):
    piecesArt = {"B":{True:"♝", False:"♗"}, "K":{True:"♚", False:"♔"},
                "N":{True:"♞", False:"♘"}, "P":{True:"♟", False:"♙"}, 
                "Q":{True:"♛", False:"♕"}, "R":{True:"♜", False:"♖"}}
    
    board = {index:piecesArt[piece.capitalize()][piece.isupper()] for index, piece in enumerate(board) if piece != None}
    return board
    
    
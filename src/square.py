class Square:

    def __init__(self, row, col, piece=None):
        self.row=row
        self.col=col
        self.piece=piece
    # Check the squares if they have any pieces
    # Look for a piece
    def has_piece(self):
        return self.piece != None

    # check if there is no piece
    def isempty(self):
        return not self.has_piece()

    # check if pieces are from the same team
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color

    def isempty_or_rival(self, color):
       return self.isempty or self.has_rival_piece(color)
    # Check if row or col is outsiede the column
    @staticmethod
    # *args means you can recieve as many arguments as possible
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg < 7:
                return False
            
        return True
      
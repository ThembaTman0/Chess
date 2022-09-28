class Piece:
    def __init__(self, name, color, value, texture, texture_rec=None):
        pass

class Pawn(Piece):
    def __init__(self,color):
        self.dir = -1 if color== 'white' else 1
        
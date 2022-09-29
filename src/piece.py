class Piece:
    def __init__(self, name, color, value, texture= None, texture_rec=None):
        pass

class Pawn(Piece):
    def __init__(self,color):
        self.dir = -1 if color== 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):

    def __init__(self,color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):
    
    def __init__(self,color):
        super().__init__('bishop', color, 3.001)
        
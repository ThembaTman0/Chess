from shutil import move
from typing import final
from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)] 

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, piece, row, col):
        # Calculate all the possible moves of an specifuc piece on a specific position
        def pawn_moves():
            steps = 1 if piece.moved else 2
            # Vertical moves
            start = row + piece.dir
            end = row + ( piece.dir * (1 + steps))
            for possible_move_row in range(start,  end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # Create initial and final move squares
                        initial= Square(row, col)
                        final= Square(possible_move_row, col)

                        # Create a new move
                        move=Move(initial, final)
                        piece.add_move(move)
                    # We cant move forward anymore
                    else:
                        break
                # not in range
                else:
                    break

            # Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        initial= Square(row, col)
                        final= Square(possible_move_row, possible_move_col)

                        # Create a new move
                        move=Move(initial, final)
                        piece.add_move(move)

        def knight_moves():
            # 8 possible moves if knight is at the center
            possible_moves= [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                # check is square is inside or out side the board
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create square of the new move
                        initial =Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        # create a new move
                        move = Move(initial, final)

                        # append new valid move
                        piece.add_move(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create squares of the possible new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create possible new move
                        move = Move(initial, final)
                        # Empty (Can i move)
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append a new move
                            piece.add_move(move)
                        
                        # has enemy piece ( There is an enemy piece breake the while true loop)
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            # append a new move
                            piece.add_move(move)
                            break
                        
                        # Has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    # If not in range
                    else: break 
                    # Increaments     
                    possible_move_row = possible_move_row + row_incr 
                    possible_move_col =  possible_move_col + col_incr

        def king_moves():
            adjs = [
                (row-1, col+0), # Up
                (row-1, col+1), # Up-Right
                (row+0, col+1), # Right
                (row+1, col+1), # Down-Right
                (row+1, col+0), # Down
                (row+1, col-1), # Down-Left
                (row+0, col-1), # Left
                (row-1, col-1) # Up-Left

            ]

            # Normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move
                # check is square is inside or out side the board
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create square of the new move
                        initial =Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        # create a new move
                        move = Move(initial, final)

                        # append new valid move
                        piece.add_move(move)
            # Castling moves

            # Queen Castling

            # King Castling
        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1, 1), # Up-Right diagonal
                (-1, -1), # Up-Left diagonal
                (1, 1), # Down-Right diagonal
                (1, -1), # Down-Left diagonal
                
            ])

        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0), # Up
                (0, 1), # Right
                (1, 0), # Down
                (0, -1), # Left
                
            ])

        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1), # Up-Right diagonal
                (-1, -1), # Up-Left diagonal
                (1, 1), # Down-Right diagonal
                (1, -1), # Down-Left diagonal
                (-1, 0), # Up
                (0, 1), # Right
                (1, 0), # Down
                (0, -1), # Left
            ])

        elif isinstance(piece, King):
            king_moves()




    def _create(self):
        

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
        

    def _add_pieces(self,color):

        row_pawn, row_other = (6, 7) if color == 'white' else  (1, 0)
        # Create the peices
        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] =  Square(row_pawn, col, Pawn(color))


        # Knights
        self.squares[row_other][1]=Square(row_other, 1, Knight(color))
        self.squares[row_other][6]=Square(row_other, 6, Knight(color))
        
        # Bishops
        self.squares[row_other][2]=Square(row_other, 2, Bishop(color))
        self.squares[row_other][5]=Square(row_other, 5, Bishop(color))


        # Bishops
        self.squares[row_other][0]=Square(row_other, 0, Rook(color))
        self.squares[row_other][7]=Square(row_other, 7, Rook(color))
        self.squares[5][5]=Square(5, 5, Rook(color))
        # Queen
        self.squares[row_other][3]=Square(row_other, 3, Queen(color))
        self.squares[4][3]=Square(4, 3, Queen(color))
        # King
        self.squares[row_other][4]=Square(row_other, 4, King(color))

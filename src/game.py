from tkinter import S
import pygame 
from const import *
from board import Board
from piece import Piece

class Game:

    def __init__(self):
        self.board =Board()

    #show method

    def show_bg(sefl, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 ==0:
                    color = (234, 235, 200) # light green
                else: 
                    color = (119, 154, 88) # dark green

                rect = (col * SQSIZE, row* SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    # render the pieces
    def show_pieces(self, surface):
        for row in range(ROWS):
                for col in range(COLS):
                    # is there a piece here

                    if self.board.squares[row][col].has_piece():
                        # store the piece into a varible
                        piece = self.board.squares[row][col].piece
                        # Load image of the piece
                        img = pygame.image.load(piece.texture)
                        # center the piece
                        img_center= col * SQSIZE + SQSIZE// 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect= img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

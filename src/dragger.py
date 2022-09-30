import pygame


import pygame
from const import *

class Dragger:
    def __init__(self):
        self.piece= None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0


    def update_blit(self, surface):
        # resize the dragged piece
        self.piece.set_texture(size=80)
        texture = self.piece.texture
        # image
        img=pygame.image.load(texture)
        # center the piece in the middle of mouse cursor
        img_center=(self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    # Update the mouse movement
    # pos is a tuple i.e pos=(xcoor, ycoor)
    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos

    # Save the position coordinates
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE
    
    def drag_piece(self, piece):
        self.piece=piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False 
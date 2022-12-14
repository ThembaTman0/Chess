import sys
from typing import final
import pygame
# Import libraries from const
from const import *
from game import Game
from move import Move
from square import Square

class Main:
    def __init__(self):
        # Define the game window/ GUI
        pygame.init()
        self.screen =pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game= Game()

    def mainloop(self):
        game=self.game
        screen=self.screen
        board=self.game.board
        dragger = self.game.dragger


        while True:
            # Render 
            # Game.py renders the objects 
            # main.py outputs the rendered object
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
            for event in pygame.event.get():
                # check if mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if the clicked square has a piece?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece= board.squares[clicked_row][clicked_col].piece
                        # if the piece is dragged save its coord
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        #SHow methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                    
                # check if mouse is moving
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE

                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final =Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)

                            # Show methods
                            game.show_bg(screen)
                            game.show_pieces(screen)

                    dragger.undrag_piece()
                # Close/Quit the GUI/Application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
        
            pygame.display.update()

main = Main()
main.mainloop()
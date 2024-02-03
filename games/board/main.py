# main.py

import pygame
import sys
from peice import Piece
import board

width = 600
height = 600

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
game_board = board.Board(width, height, 10, 10, screen)
piece = Piece("red", (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Get the mouse coordinates
                mouse_x, mouse_y = event.pos

                # Convert mouse coordinates to board coordinates
                cell_width = width // game_board.columns
                cell_height = height // game_board.rows
                col_index = mouse_x // cell_width
                row_index = mouse_y // cell_height

                # Move the piece to the clicked board coordinates
                piece.move((col_index * cell_width, row_index * cell_height))

    screen.fill((255, 255, 255))
    piece.draw_piece(screen)
    game_board.draw_board(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

from peice import Piece
from typing import List, Tuple, Dict, Union, Optional
import pygame

class Board:
    def __init__(self,width,height, rows, columns, screen):
        self.screen = screen
        self.rows = rows
        self.width = width
        self.height = height
        self.columns = columns
        self.grid: List[List[Optional[Piece]]] = [[None for y in range(columns)] for x in range(rows)]
        self.initialize_board()

    def initialize_board(self):
        self.draw_board(self.screen)
        # Logic to initialize the board with pieces at their starting positions
        pass

    def draw_board(self,screen):
        cell_width = self.width // self.columns
        cell_height = self.height // self.rows

        # Draw horizontal lines
        for row in range(self.rows + 1):
            pygame.draw.line(screen, "black", (0, row * cell_height), (self.width, row * cell_height))

        # Draw vertical lines
        for col in range(self.columns + 1):
            pygame.draw.line(screen, "black", (col * cell_width, 0), (col * cell_width, self.height))

        # Draw pieces
        for row_index, row in enumerate(self.grid):
            for col_index, piece in enumerate(row):
                if piece:
                    x = col_index * cell_width + cell_width // 2
                    y = row_index * cell_height + cell_height // 2
                    piece.draw_piece(screen, x, y)

    def move_piece(self, piece, destination: Tuple[int, int]):
        #TODO using move_piece of the board
        #TODO get the piece out of the borad

        #if destination
        # Logic to update the board state after a piece has moved
        pass

    def get_piece_at(self, position):
        #TODO return the current positon of the piece
        # Logic to retrieve information about the piece at a specific position on the board
        pass

    def is_valid_move(self, piece, destination):
        #TODO
        # Logic to check if a move is valid before applying it to the board
        pass

    def remove_piece(self, piece):
        # Logic to remove a piece from the board
        pass
    def add_piece(self,piece):
        pass




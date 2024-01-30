import peice
from typing import List, Tuple, Dict, Union
import pygame

class Board:
    def __init__(self, rows, columns, piece: Tuple[str,int,int,int]):
        self.rows = rows
        self.columns = columns
        #the thrid element in piece tuple represent the color of the piece
        #0-is non color
        #1-is x color
        #2- is y color and so on
        self.piece = piece
        self.grid = [[0 for y in range(columns)] for x in range(rows)]
        self.initialize_board()

    def initialize_board(self):
        self.screen = pygame.display.set_mode((self.rows,self.columns))
        pygame.display.set_caption("board game")
        self.draw_board()
        # Logic to initialize the board with pieces at their starting positions
        pass

    def draw_board(self):
        # Logic to draw the current state of the board
        for row in self.grid:
            print(" ".join(map(str, row)))

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




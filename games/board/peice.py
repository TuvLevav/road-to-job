import pygame
from board import Board
class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw_piece(self, screen,piece, cell_width, cell_height):
        x, y = self.position
        pygame.draw.circle(screen, self.color, (x * cell_width + cell_width // 2, y * cell_height + cell_height // 2), 20)

    def move(self, destination,screen):
        # Logic for moving the piece
        self.position = destination


    def get_valid_moves(self, board):
        #TODO Get a list of valid moves for the piece on the given board.
        #TODO Placeholder for future implementation.
        pass

        #Implement logic to get a list of valid moves for the piece on the given board

    def is_valid_move(self, destination, board):
        # TODO for array- checking if this index, x and y in range of the board
        # TODO if the x,y index in the  range of the borad i decide
        # Implement logic to check if a specific move is valid for the piece on the given board
        pass


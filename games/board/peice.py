import pygame

class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw_piece(self, screen, x, y):
        pygame.draw.circle(screen, self.color, (x, y), 20)
        # Implement logic to draw/render the piece on the game board
        pass

    def move(self, destination):
        # Logic for moving the piece
        self.position = destination

    def get_valid_moves(self, board):
        #TODO Get a list of valid moves for the piece on the given board.
        #TODO Placeholder for future implementation.

        # Implement logic to get a list of valid moves for the piece on the given board
        pass

    def is_valid_move(self, destination, board):
        # TODO for array- checking if this index, x and y in range of the board
        # TODO if the x,y index in the  range of the borad i decide
        # Implement logic to check if a specific move is valid for the piece on the given board
        pass


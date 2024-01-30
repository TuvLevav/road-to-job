import board
import pygame
import sys

board = board.Board(25, 30, ("a", (2, 3), 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

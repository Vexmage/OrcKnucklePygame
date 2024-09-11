import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set window size and title
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OrcKnuckle")

def main():
    game = Game(screen)  # Pass the screen to the Game class
    game.start()

if __name__ == "__main__":
    main()

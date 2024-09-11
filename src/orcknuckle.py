
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
    # Create a new instance of the Game class
    game = Game(screen)

    # Start the game
    game.start()

if __name__ == "__main__":
    main()

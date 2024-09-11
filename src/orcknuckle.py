import pygame
from game import Game  # Ensure the Game class is imported from the game module

def main():
    # Initialize Pygame
    pygame.init()

    # Set window size and title
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("OrcKnuckle")

    # Run the game
    game = Game(screen)  # Pass the Pygame screen to the Game class
    game.start()

    pygame.quit()

if __name__ == "__main__":
    main()

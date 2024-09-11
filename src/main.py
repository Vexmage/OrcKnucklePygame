import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set window size and title
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OrcKnuckle")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set font
font = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    """Helper function to render text on the screen."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    # Initialize the game object
    game = Game()

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)  # Clear the screen

        # Check for events (keyboard/mouse/etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display some placeholder text
        draw_text("Welcome to OrcKnuckle", font, BLACK, screen, 20, 20)

        # Add more game logic and drawing here...

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

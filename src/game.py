import pygame
import time

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OrcKnuckle")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set font
font = pygame.font.SysFont(None, 36)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True  # Control the main game loop

    def draw_text(self, text, x, y):
        """Helper function to render text on the screen."""
        text_surface = font.render(text, True, BLACK)
        self.screen.blit(text_surface, (x, y))

    def main_loop(self):
        """Main game loop that handles Pygame events."""
        while self.running:
            self.screen.fill(WHITE)  # Clear the screen to white

            # Basic event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw some basic text to show the window is running
            self.draw_text("Welcome to OrcKnuckle!", 200, 100)

            # Update the display
            pygame.display.update()

            time.sleep(0.01)  # Delay to make the loop less CPU intensive

        pygame.quit()

    def start(self):
        """Start the main game loop."""
        self.main_loop()

# Main function to run the game
if __name__ == "__main__":
    game = Game(screen)
    game.start()

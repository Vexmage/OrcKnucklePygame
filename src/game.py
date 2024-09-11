import pygame
from player import HumanPlayer, ComputerPlayer
from dice import Dice
from collections import Counter
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
    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.running = True  # Control the main game loop

    def draw_text(self, text, x, y):
        """Helper function to render text on the screen."""
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x, y))

    def add_player(self):
        """Add human or computer players."""
        num_players = int(input("Enter the number of players: "))
        for i in range(1, num_players + 1):
            name = input(f"Enter the name of Player {i}: ")
            player_type = input(f"Is {name} a human or computer player? (human/computer): ").lower()
            if player_type == "human":
                self.players.append(HumanPlayer(name))
            else:
                self.players.append(ComputerPlayer(name))

    def play_round(self):
        """Play one round of the game where each player rolls."""
        screen.fill(WHITE)  # Clear the screen for each round
        y_offset = 20  # Start position for displaying rolls

        for player in self.players:
            player.roll_knuckles(self.dice)
            time.sleep(1)  # Adds suspense

            # Display the player's rolls on the screen
            self.draw_text(f"{player.name} rolled:", 20, y_offset)
            y_offset += 40  # Space between the player's name and their rolls

            for rune, knuckle_type in player.rolls:
                self.draw_text(f"{knuckle_type.capitalize()} shows a {rune.capitalize()} ({player.rune_values[rune]} points)", 40, y_offset)
                y_offset += 40  # Space between each dice roll

            pygame.display.update()  # Update the display after each player's rolls

            if y_offset > WINDOW_HEIGHT - 100:
                time.sleep(2)  # Delay to allow players to see the current text
                screen.fill(WHITE)  # Reset screen to prevent clutter
                y_offset = 20  # Reset offset for next player

    def pause_for_next_round(self):
        """Pause the game and wait for player input before continuing."""
        waiting = True
        self.draw_text("Press any key to start the next round, or press ESC to quit.", 20, WINDOW_HEIGHT - 50)
        pygame.display.update()

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        waiting = False
                    else:
                        waiting = False  # Continue to next round if any other key is pressed

    def main_loop(self):
        """Main game loop that handles Pygame events."""
        while self.running:
            screen.fill(WHITE)  # Clear the screen each frame

            # Call game logic (play rounds)
            self.play_round()

            # Pause for input before starting the next round
            self.pause_for_next_round()

            # Continuously refresh the screen
            pygame.display.update()

        pygame.quit()

    def start(self):
        """Start the game, set up players, and manage rounds."""
        self.add_player()
        self.main_loop()


# Example game setup and start
if __name__ == "__main__":
    game = Game()
    game.start()

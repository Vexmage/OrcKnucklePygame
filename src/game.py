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
    def __init__(self, screen):
        self.players = []
        self.dice = Dice()
        self.screen = screen
        self.running = True
        self.input_active = True
        self.current_input = ""
        self.player_inputs = []

    def draw_text(self, text, x, y):
        """Helper function to render text on the screen."""
        text_surface = font.render(text, True, BLACK)
        self.screen.blit(text_surface, (x, y))

    def get_text_input(self, prompt, y_offset):
        """Handle text input for player setup."""
        waiting = True
        input_box = ""

        while waiting:
            self.screen.fill(WHITE)
            self.draw_text(prompt, 20, y_offset)
            self.draw_text(input_box, 20, y_offset + 40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_box = input_box[:-1]  # Remove the last character
                    else:
                        input_box += event.unicode  # Add the new character

            pygame.display.update()
        
        return input_box

    def add_player(self):
        """Add human or computer players via GUI."""
        num_players = int(self.get_text_input("Enter the number of players:", 100))

        for i in range(1, num_players + 1):
            player_name = self.get_text_input(f"Enter name for Player {i}:", 150)
            player_type = self.get_text_input(f"Is {player_name} a human or computer? (human/computer):", 200).lower()
            
            if player_type == "human":
                self.players.append(HumanPlayer(player_name))
            else:
                self.players.append(ComputerPlayer(player_name))

    def apply_cancellation(self):
        """Handle rune cancellation between players."""
        rune_counts = {player.name: Counter([rune for rune, _ in player.rolls]) for player in self.players}
        self.screen.fill(WHITE)
        y_offset = 20

        # Iterate over each player's runes and cancel them accordingly
        while True:
            made_cancellation = False
            for player in self.players:
                for opponent in self.players:
                    if player.name != opponent.name:
                        # Ghost cancels Princess
                        if rune_counts[player.name]['ghost'] > 0 and rune_counts[opponent.name]['princess'] > 0:
                            if isinstance(player, HumanPlayer):
                                candidates = [
                                    opp.name for opp in self.players
                                    if opp.name != player.name and rune_counts[opp.name]['princess'] > 0
                                ]
                                if len(candidates) > 0:
                                    chosen_target = player.choose_target(candidates)
                                    self.draw_text(f"{player.name}'s ghost cancels {chosen_target}'s princess!", 20, y_offset)
                                    y_offset += 40
                                    rune_counts[player.name]['ghost'] -= 1
                                    rune_counts[chosen_target]['princess'] -= 1
                                    made_cancellation = True
                            else:
                                self.draw_text(f"{player.name}'s ghost cancels {opponent.name}'s princess!", 20, y_offset)
                                y_offset += 40
                                rune_counts[player.name]['ghost'] -= 1
                                rune_counts[opponent.name]['princess'] -= 1
                                made_cancellation = True

                        # Knight cancels Dragon
                        if rune_counts[player.name]['knight'] > 0 and rune_counts[opponent.name]['dragon'] > 0:
                            if isinstance(player, HumanPlayer):
                                candidates = [
                                    opp.name for opp in self.players
                                    if opp.name != player.name and rune_counts[opp.name]['dragon'] > 0
                                ]
                                if len(candidates) > 0:
                                    chosen_target = player.choose_target(candidates)
                                    self.draw_text(f"{player.name}'s knight cancels {chosen_target}'s dragon!", 20, y_offset)
                                    y_offset += 40
                                    rune_counts[player.name]['knight'] -= 1
                                    rune_counts[chosen_target]['dragon'] -= 1
                                    made_cancellation = True
                            else:
                                self.draw_text(f"{player.name}'s knight cancels {opponent.name}'s dragon!", 20, y_offset)
                                y_offset += 40
                                rune_counts[player.name]['knight'] -= 1
                                rune_counts[opponent.name]['dragon'] -= 1
                                made_cancellation = True

            if not made_cancellation:
                break

        pygame.display.update()
        return rune_counts

    def play_round(self):
        """Play one round of the game where each player rolls."""
        self.screen.fill(WHITE)
        y_offset = 20

        for player in self.players:
            player.roll_knuckles(self.dice)
            time.sleep(1)  # Adds suspense

            # Display the player's rolls on the screen
            self.draw_text(f"{player.name} rolled:", 20, y_offset)
            y_offset += 40

            for rune, knuckle_type in player.rolls:
                self.draw_text(f"{knuckle_type.capitalize()} shows a {rune.capitalize()} ({player.rune_values[rune]} points)", 40, y_offset)
                y_offset += 40

            pygame.display.update()

            if y_offset > WINDOW_HEIGHT - 100:
                time.sleep(2)
                self.screen.fill(WHITE)
                y_offset = 20

        final_runes = self.apply_cancellation()
        self.calculate_scores(final_runes)

    def calculate_scores(self, final_runes):
        """Calculate and display the scores after cancellations."""
        y_offset = 20
        self.screen.fill(WHITE)
        for player in self.players:
            rune_count = final_runes[player.name]
            score = sum(player.rune_values[rune] * count for rune, count in rune_count.items())
            player.score = score
            self.draw_text(f"After cancellation, {player.name} has a score of {score} points.", 20, y_offset)
            y_offset += 40
        pygame.display.update()

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
                        waiting = False

    def main_loop(self):
        """Main game loop that handles Pygame events."""
        while self.running:
            self.screen.fill(WHITE)
            self.play_round()
            self.pause_for_next_round()
            pygame.display.update()

        pygame.quit()

    def start(self):
        """Start the game, set up players, and manage rounds."""
        self.add_player()
        self.main_loop()

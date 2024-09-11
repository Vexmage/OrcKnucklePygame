import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OrcKnuckle Player Setup")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set font
font = pygame.font.SysFont(None, 36)

# Function to draw text on screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Input box class for handling player input
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the input box
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = BLACK if self.active else GRAY

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text  # Return input on Enter key press
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # Delete character
                else:
                    self.text += event.unicode  # Add character

                # Update text surface
                self.txt_surface = font.render(self.text, True, BLACK)

    def draw(self, screen):
        # Draw text box
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


# Main game loop
def main():
    # Set up input boxes for number of players, names, and types
    input_box = InputBox(200, 150, 400, 40)
    input_boxes = [input_box]
    player_inputs = []  # Store player names and types
    current_step = 0  # 0 = number of players, 1 = entering names, 2 = selecting type
    num_players = None
    current_player = 0  # Track which player's name/type we're getting

    running = True

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle input events
            if current_step == 0:
                num_players = input_box.handle_event(event)
            elif current_step == 1:
                player_name = input_boxes[current_player].handle_event(event)
                if player_name:
                    player_inputs.append({'name': player_name, 'type': None})
                    current_player += 1
            elif current_step == 2:
                player_type = input_boxes[current_player].handle_event(event)
                if player_type in ['human', 'computer']:
                    player_inputs[current_player]['type'] = player_type
                    current_player += 1

        # Draw input boxes and prompts
        if current_step == 0:
            draw_text("Enter the number of players:", 200, 100)
            input_box.draw(screen)
            if num_players and num_players.isdigit():
                num_players = int(num_players)
                input_boxes = [InputBox(200, 150, 400, 40) for _ in range(num_players)]
                current_step = 1  # Move to name input step

        elif current_step == 1:
            if current_player < num_players:
                draw_text(f"Enter the name of Player {current_player + 1}:", 200, 100)
                input_boxes[current_player].draw(screen)
            else:
                current_player = 0
                input_boxes = [InputBox(200, 150, 400, 40) for _ in range(num_players)]
                current_step = 2  # Move to type selection

        elif current_step == 2:
            if current_player < num_players:
                draw_text(f"Is {player_inputs[current_player]['name']} a human or computer player?", 200, 100)
                input_boxes[current_player].draw(screen)
            else:
                print(player_inputs)
                break  # All inputs are done, exit game setup

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

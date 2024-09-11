import pygame

def input_box(screen, x, y, width, height, prompt):
    """Display a text input box and return the entered text."""
    font = pygame.font.SysFont(None, 36)
    input_active = False
    input_text = ''
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    input_rect = pygame.Rect(x, y, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
                color = color_active if input_active else color_inactive
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        return input_text  # Return the entered text when pressing Enter
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]  # Remove the last character
                    else:
                        input_text += event.unicode  # Add typed characters

        screen.fill((255, 255, 255))  # White background
        # Render the prompt
        prompt_surface = font.render(prompt, True, (0, 0, 0))
        screen.blit(prompt_surface, (x, y - 40))  # Show prompt above input box
        # Render the current input text
        txt_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, color, input_rect, 2)

        pygame.display.flip()

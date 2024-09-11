import pygame

def draw_text(screen, text, x, y, font_size=36, color=(0, 0, 0)):
    """Helper function to render text on the screen."""
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def input_box(screen, x, y, width, height, prompt):
    """Helper function for a user input box."""
    input_active = False
    color = (200, 200, 200)
    user_text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.fill((255, 255, 255))
        draw_text(screen, prompt, x, y - 40, 24)
        pygame.draw.rect(screen, color, (x, y, width, height), 2)

        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (x + 5, y + 5))
        pygame.display.update()

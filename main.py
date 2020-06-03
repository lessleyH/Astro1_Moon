import pygame
from menu import*

# Define constants for the screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 720


def main():
    pygame.init()
    pygame.display.set_caption("Origins of the Moon")

    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)

        if game_state == GameState.FORMATION_LEVEL:
            game_state = play_level(screen)

        if game_state == GameState.EARTHMOON_LEVEL:
            game_state = play_level(screen)
        
        if game_state == GameState.MOONAGE_LEVEL:
            game_state = play_level(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()
import pygame
from menu import*
from phases import earth_moon
from surface import age_moon
from theia import theia_moon

if getattr(sys, 'assets', False):
    os.chdir(sys._MEIPASS)

# Define constants for the screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 720


def main():
    pygame.init()
    pygame.font.init()


    pygame.display.set_caption("Origins of the Moon")
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    game_state = GameState.TITLE

    current_level = 0
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)

        if game_state == GameState.FORMATION_LEVEL:
            current_level += 1
            game_state = theia_moon(screen)

        if game_state == GameState.EARTHMOON_LEVEL:
            current_level += 1
            game_state = earth_moon(screen)
        
        if game_state == GameState.MOONAGE_LEVEL:
            current_level += 1
            game_state = age_moon(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()
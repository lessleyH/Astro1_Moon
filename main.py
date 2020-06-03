import pygame
from menu import*
from phases import earth_moon
from surface import age_moon

# Define constants for the screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 720

def main():
    pygame.init()
    pygame.display.set_caption("Origins of the Moon")

    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    game_state = GameState.TITLE

    pygame.mixer.music.load('./assets/epic_soundtrack.wav')
    pygame.mixer.music.play(-1)

    current_level = 0

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)
            print(current_level)

        if game_state == GameState.FORMATION_LEVEL:
            current_level += 1
            print(current_level)
            game_state = play_level(screen)

        if game_state == GameState.EARTHMOON_LEVEL:
            current_level += 1
            print(current_level)
            game_state = earth_moon(screen)
        
        if game_state == GameState.MOONAGE_LEVEL:
            current_level += 1
            print(current_level)
            game_state = age_moon(screen)

        if game_state == GameState.QUIT:
            print(current_level)
            pygame.quit()
            return

        print(current_level)

if __name__ == "__main__":
    main()
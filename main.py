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
            player = Player()
            game_state = play_level(screen, player)
            print(player.current_level)

        if game_state == GameState.FORMATION_LEVEL:
            player.current_level += 1
            print(player.current_level)
            game_state = play_level(screen, player)

        if game_state == GameState.EARTHMOON_LEVEL:
            player.current_level += 1
            print(player.current_level)
            game_state = play_level(screen, player)
        
        if game_state == GameState.MOONAGE_LEVEL:
            player.current_level += 1
            print(player.current_level)
            game_state = play_level(screen, player)

        if game_state == GameState.QUIT:
            print(player.current_level)
            pygame.quit()
            return
        print(player.current_level)

if __name__ == "__main__":
    main()
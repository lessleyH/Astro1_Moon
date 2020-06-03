import pygame
import random

# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 720

# Define the moon object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super(Moon, self).__init__()
        self.surf = pygame.image.load("./assets/moon.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the moon based on a constant speed
    # Remove the moon when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()

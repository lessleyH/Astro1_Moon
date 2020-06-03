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


# Define the asteroid object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'asteroid'
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.surf = pygame.image.load("./assets/asteroid.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
import pygame
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

#Stores information about a player
class Player:
    def __init__(self, current_level=1):
        super(Player,  self).__init__()
        self.surf = pygame.image.load("./assets/jeyL.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.current_level = current_level
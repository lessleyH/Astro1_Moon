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
# Define constants for the screen width and height
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 720


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self,current_level=0):
        super(Player, self).__init__()
        player_img = pygame.image.load("./assets/jeyL.png")
        player_img = pygame.transform.scale(player_img, (50, 50))
        self.surf = player_img.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.current_level = current_level
        self.wrap = False

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -50)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 50)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-50, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(50, 0)

        if self.rect.x == 0:
            # off screen left
            self.rect.move_ip(SCREEN_WIDTH, 0)
            self.wrap = True

        if self.rect.x  + 50 > SCREEN_WIDTH:
            # off screen right
            self.rect.move_ip(-SCREEN_WIDTH, 0)
            self.wrap = True
        
        if self.rect.y  <0:
            # off screen top
            self.rect.move_ip(0,SCREEN_HEIGHT)
            self.wrap = True

        if self.rect.y + 50 > SCREEN_HEIGHT:
            # off screen bottom
            self.wrap = True

import pygame
import random
import math
from player import*
from asteroid import*
from moon import*

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
size = (SCREEN_WIDTH, SCREEN_HEIGHT)

#stat pygame 
pygame.init()
pygame.display.set_caption("Origins of the Moon")
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# background surfaces
background = pygame.image.load("./assets/bg.jpg")
background = pygame.transform.scale(background, (size))
background = background.convert()
background_rect = background.get_rect()


# Instantiate player. Right now, this is just a rectangle.
player = Player()


# Create a custom event for adding a new asteroid
# ADDASTER = pygame.USEREVENT + 1
# pygame.time.set_timer(ADDASTER, 2030)
# ADDMOON = pygame.USEREVENT + 2
# pygame.time.set_timer(ADDMOON, 10000)



# Create groups to hold asteroid sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
# enemies = pygame.sprite.Group()
# moons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:
    win.blit(background, (0, 0))

    # Did the user click the window close button?
    for event in pygame.event.get():

        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        # Add a new asteroid?
        # elif event.type == ADDASTER:
        #     # Create the new asteroid and add it to sprite groups
        #     new_aster = Asteroid()
        #     enemies.add(new_aster)
        #     all_sprites.add(new_aster)
        
         # Add a new MOON?
        # elif event.type == ADDMOON:
        #     # Create the new MOON and add it to sprite groups
        #     new_moon = Moon()
        #     moons.add(new_moon)
        #     all_sprites.add(new_moon)

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    # enemies.update()
    # moons.update()

    # Fill the background with white
    # win.fill((0, 0, 0))
    # Draw all sprites
    for entity in all_sprites:
        win.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    # if pygame.sprite.spritecollideany(player, enemies):
    #     # If so, then remove the player and stop the loop
    #     player.kill()
    #     running = False

    # # Create a surface and pass in a tuple containing its length and width
    # surf = pygame.Surface((50, 50))

    # surf.fill((255, 0, 0))
    # rect = surf.get_rect()

    # s_center = ((SCREEN_WIDTH-surf.get_width())/2,
    # (SCREEN_HEIGHT-surf.get_height())/2)

    # win.blit(surf, s_center)

    # Draw the player on the screen
    win.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
pygame.quit()



# lots o' imports
import sys, pygame
import os.path
filepath = os.path.dirname(__file__)

# constants
size = width, height = 1040, 720 # pixels
km_to_pixel = 0.0022 # real world units to computer screen units
earth_diameter = 6378.1*2 # km
moon_diameter = 1738.1*2 # km
lunar_distance = 384400 # km

# initialize game
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lessley & Aadil\'s Creative Project')

# load images
background = pygame.image.load(os.path.join(filepath, "images/space.jpg"))
background = pygame.transform.scale(background, size)
background = background.convert()
background_rect = background.get_rect()

earth_above = pygame.image.load(os.path.join(filepath, "images/earth_from_above.png"))
earth_above = pygame.transform.scale(earth_above, (int(earth_diameter*km_to_pixel), int(earth_diameter*km_to_pixel)))
earth_above = earth_above.convert()
earth_above_rect = earth_above.get_rect()
earth_above_rect.centerx, earth_above_rect.centery = width/10, height/2#width/2, height/2

moon_above = pygame.image.load(os.path.join(filepath, "images/moon_from_above.png"))
moon_above = pygame.transform.scale(moon_above, (int(moon_diameter*km_to_pixel), int(moon_diameter*km_to_pixel)))
moon_above = moon_above.convert()
moon_above_rect = moon_above.get_rect()
moon_above_rect.centerx, moon_above_rect.centery = earth_above_rect.centerx + int(lunar_distance*km_to_pixel), earth_above_rect.centery

# animation loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # display
    screen.blit(background, (0, 0))
    screen.blit(earth_above, earth_above_rect)
    screen.blit(moon_above, moon_above_rect)
    pygame.display.update()
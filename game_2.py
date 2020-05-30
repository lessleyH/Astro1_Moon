# lots o' imports
import sys, pygame
import os.path
import math
filepath = os.path.dirname(__file__)

# constants
size = width, height = 1040, 720 # pixels
km_to_pixel = 0.0008 # real world units to computer screen units
earth_diameter = 6378.1*2 # km
moon_diameter = 1738.1*2 # km
lunar_distance = 384400 # km
zoom_size = 100 # window for seeing phases
WHITE = (255,255,255) # colors
BLACK = (0,0,0)

# initialize game
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lessley & Aadil\'s Creative Project')

# load images
background = pygame.image.load(os.path.join(filepath, "images/space.jpg"))
background = pygame.transform.scale(background, size)
background = background.convert()
background_rect = background.get_rect()

earth = pygame.image.load(os.path.join(filepath, "images/earth_from_above_shadow.png"))
earth = pygame.transform.scale(earth, (int(earth_diameter*km_to_pixel), int(earth_diameter*km_to_pixel)))
earth = earth.convert()
earth_rect = earth.get_rect()
earth_rect.centerx, earth_rect.centery = width/2, height/2

moon = pygame.image.load(os.path.join(filepath, "images/moon_from_above.png"))
moon = pygame.transform.scale(moon, (int(moon_diameter*km_to_pixel), int(moon_diameter*km_to_pixel)))
moon = moon.convert()
moon_rect = moon.get_rect()
moon_rect.centerx, moon_rect.centery = earth_rect.centerx, earth_rect.centery-int(lunar_distance*km_to_pixel)

arrow = pygame.image.load(os.path.join(filepath, "images/arrow.png"))
arrow = pygame.transform.scale(arrow, (30, 10))
arrow_rect = arrow.get_rect()
arrow_rect.centerx, arrow_rect.centery = arrow_rect.centerx, arrow_rect.centery-arrow.get_height()/2

zoom_border = pygame.Rect(arrow_rect.centerx + arrow_rect.width, arrow_rect.centery - zoom_size/2, zoom_size, zoom_size)
zoom = pygame.Rect(arrow_rect.centerx + arrow_rect.width + 2, arrow_rect.centery - zoom_size/2 + 2, zoom_size-4, zoom_size-4)

moon_zoomed = pygame.image.load(os.path.join(filepath, "images/moon_from_above_shadow.png"))
moon_zoomed = pygame.transform.scale(moon_zoomed, (int(zoom_size*0.8), int(zoom_size*0.8)))
moon_zoomed.convert()
moon_zoomed_rect = moon_zoomed.get_rect()
moon_zoomed_rect.center = zoom.center

phase_border = pygame.Rect(earth_rect.centerx + 5*earth_rect.width, earth_rect.centery - zoom_size/2, zoom_size, zoom_size)

phases = []
for i in range(1, 8+1):
    phase = pygame.image.load(os.path.join(filepath, "images/phases", str(i)+".png"))
    phase = pygame.transform.scale(phase, (int(zoom_size*0.8),int(zoom_size*0.8)))
    phase.convert()
    phase_rect = phase.get_rect()
    phase_rect.center = phase_border.center
    phases.append((phase, phase_rect))

angle = 0
speed = 50
next_tick = 500
radius = int(lunar_distance*km_to_pixel)
phase_i = 0

def move_coords(angle, radius):
    theta = math.radians(angle)
    return (earth_rect.centerx + radius * math.cos(theta), earth_rect.centery + radius * math.sin(theta))

# animation loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # move moon in orbit
    ticks = pygame.time.get_ticks() 
    if ticks > next_tick:
        next_tick += speed
        angle -= 1
        angle %= 360
        moon_rect.center = move_coords(angle, radius)
        arrow_rect.center = moon_rect.left + arrow_rect.width, moon_rect.top
        zoom_border.center = arrow_rect.centerx + 2.5*arrow_rect.width, arrow_rect.centery
        zoom.center = zoom_border.center
        moon_zoomed_rect.center = zoom.center

    # display
    screen.blit(background, (0, 0))
    screen.blit(earth, earth_rect)
    pygame.draw.rect(screen, WHITE, phase_border, 2)
    screen.blit(*phases[phase_i])
    screen.blit(moon, moon_rect)
    screen.blit(arrow, arrow_rect)
    pygame.draw.rect(screen, WHITE, zoom_border, 2)
    pygame.draw.rect(screen, BLACK, zoom, 0)
    screen.blit(moon_zoomed, moon_zoomed_rect)
    pygame.display.update()
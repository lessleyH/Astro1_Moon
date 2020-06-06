import os, sys
import pygame
from menu import GameState,resource_path

# get location of file
file_path = os.path.dirname(__file__)
if getattr(sys, 'assets', False):
    os.chdir(sys._MEIPASS)

# constants
size = width, height = 1040, 720 # pixels
km_to_pixel = 0.175 # real world units to computer screen units
mars_diameter = 6779 # km
proto_earth_diameter = 12742 #km
WHITE = (255, 255, 255) # colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
button_radius = 15
order_d = {  14:'Moon',
                1:'Apollo',
                0:'Space',
                3:'Proto-Earth',
                6:'Theia Impact',
                8:'Theia Graze',
                11:'Orbit',
                10:'Our Moon'}


def theia_moon(screen):
    ### LOAD SURFACES ###

    # background surfaces
    space = pygame.image.load(resource_path("assets/space.jpg"))
    space = pygame.transform.scale(space, size)
    space = space.convert()
    space_rect = space.get_rect()

    # background surfaces
    orbit = pygame.image.load(resource_path("assets/gih/orbitEarth.jpg"))
    orbit = pygame.transform.scale(orbit, size)
    orbit = orbit.convert()
    orbit_rect = orbit.get_rect()

    # background surfaces
    apollo = pygame.image.load(resource_path("assets/gih/apollo.jpg"))
    apollo = pygame.transform.scale(apollo, size)
    apollo = apollo.convert()
    apollo_rect = apollo.get_rect()

    # background surfaces
    moon = pygame.image.load(resource_path("assets/gih/moon.png"))
    moon = pygame.transform.scale(moon, size)
    moon = moon.convert()
    moon_rect = moon.get_rect()

    #Proto Earth 
    proto_earth = pygame.image.load(resource_path("assets/gih/protoEarth.jpg"))
    proto_earth = pygame.transform.scale(proto_earth, size)
    proto_earth = proto_earth.convert()
    proto_earth_rect = proto_earth.get_rect()

    #Theia First Impact 
    theia_impact = pygame.image.load(resource_path("assets/gih/Theia_Impact.png"))
    theia_impact = pygame.transform.scale(theia_impact, size)
    theia_impact = theia_impact.convert()
    theia_impact_rect = theia_impact.get_rect()

    #Theia Impact Explostion
    theia_2 = pygame.image.load(resource_path("assets/gih/Thea_impact3.jpg"))
    theia_2= pygame.transform.scale(theia_2, size)
    theia_2 = theia_2.convert()
    theia_2_rect = theia_2.get_rect()

    #Theia Impact Explostion
    theia_3 = pygame.image.load(resource_path("assets/gih/ring_protoearth.jpg"))
    theia_3= pygame.transform.scale(theia_3, size)
    theia_3 = theia_3.convert()
    theia_3_rect = theia_3.get_rect()

    #backgrounds
    order= {'Apollo':[apollo, apollo_rect],'Orbit':[orbit, orbit_rect],'Moon':[moon, moon_rect], 'Space': [space, space_rect], 'Proto-Earth':[proto_earth, proto_earth_rect], 'Theia Impact':[theia_impact, theia_impact_rect],'Theia Graze':[theia_2, theia_2_rect],'Our Moon':[theia_3, theia_3_rect]}

    # text surfaces
    font = pygame.font.SysFont('Sans', 18)
    title = font.render('Press the LEFT arrow to start. Have fun!,   ESC: exit,   LEFT/RIGHT: for narration', True, WHITE)
    story, topic = [], None
    with open(resource_path('assets/gih/story.txt')) as file:
        story = [font.render(line.rstrip('\n'), True, WHITE) for line in file]
    story_i= 0
    progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE, BLACK)

    ### BEGIN ANIMATION ###

    # variables
    background, background_rect = space, space_rect
    step = 0 #variable for arc
    keydown = False 

    # animation
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            # key press
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Was it the Escape key? If so, stop the loop.
                    return GameState.NEWGAME
                elif event.key == pygame.K_LEFT:
                    # move forward in story
                    if story_i > 0:
                        story_i -= 1
                        progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE, BLACK)

                elif event.key == pygame.K_RIGHT:
                    # move backward in story
                    if story_i < len(story)-1:
                        story_i += 1
                        progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE, BLACK)
 
        # display everything
        for key in order_d:
            if key == story_i: 
                background, background_rect = order[order_d[key]][0], order[order_d[key]][1]
        screen.blit(background, (0, 0))
        screen.blit(title, (width//2 - title.get_rect().width//2, title.get_rect().height))
        screen.blit(story[story_i], ((width-story[story_i].get_rect().width)//2, height-2*story[story_i].get_rect().height))
        screen.blit(progress, ((width-progress.get_rect().width-10, height-2*progress.get_rect().height)))

        # update display
        pygame.display.update()
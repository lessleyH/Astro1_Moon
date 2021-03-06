import sys
import os
import pygame
import math
from menu import GameState,resource_path
file_path = os.path.dirname(__file__)

if getattr(sys, 'assets', False):
    os.chdir(sys._MEIPASS)

# constants
size = width, height = 1040, 720 # pixels
km_to_pixel = 0.0008 # real world units to computer screen units
sun_diameter = 695508*2 # km
earth_diameter = 6378.1*2 # km
moon_diameter = 1738.1*2 # km
lunar_distance = 384400 # km
zoom_size = 75 # window for seeing phases
WHITE = (255, 255, 255) # colors
BLACK = (0, 0, 0)
phase_dict = {  0:'(5) Full',
                1:'(6) Waning Gibbous',
                2:'(7) Third Quarter',
                3:'(8) Waning Crescent',
                4:'(1) New',
                5:'(2) Waxing Crescent',
                6:'(3) First Quarter',                
                7:'(4) Waxing Gibbous'  }

def earth_moon(screen):
    ### LOAD SURFACES ###

    # background surface
    background = pygame.image.load(resource_path("assets/earth_moon/space.jpg"))
    background = pygame.transform.scale(background, size)
    background = background.convert()

    # earth surface
    earth = pygame.image.load(resource_path("assets/earth_moon/earth_from_above_shadow.png"))
    earth = pygame.transform.scale(earth, (int(earth_diameter*km_to_pixel), int(earth_diameter*km_to_pixel)))
    earth = earth.convert()
    earth_rect = earth.get_rect()
    earth_rect.centerx, earth_rect.centery = width/2, height/2

    # tiny moon surface
    moon = pygame.image.load(resource_path("assets/earth_moon/moon_from_above.png"))
    moon = pygame.transform.scale(moon, (int(moon_diameter*km_to_pixel), int(moon_diameter*km_to_pixel)))
    moon = moon.convert()
    moon_rect = moon.get_rect()
    moon_rect.centerx, moon_rect.centery = earth_rect.centerx, earth_rect.centery-int(lunar_distance*km_to_pixel)

    # arrow (pointing to tiny moon) surface
    arrow = pygame.image.load(resource_path("assets/earth_moon/arrow.png"))
    arrow = pygame.transform.scale(arrow, (30, 10))
    arrow_rect = arrow.get_rect()
    arrow_rect.centerx, arrow_rect.centery = arrow_rect.centerx, arrow_rect.centery-arrow.get_height()/2

    # zoom window suface
    zoom = pygame.Rect(arrow_rect.centerx + arrow_rect.width + 2, arrow_rect.centery - zoom_size/2 + 2, zoom_size-4, zoom_size-4)
    zoom_border = pygame.Rect(arrow_rect.centerx + arrow_rect.width, arrow_rect.centery - zoom_size/2, zoom_size, zoom_size)

    # zoomed moon surface
    moon_zoomed = pygame.image.load(resource_path("assets/earth_moon/moon_from_above_shadow.png"))
    moon_zoomed = pygame.transform.scale(moon_zoomed, (int(zoom_size*0.8), int(zoom_size*0.8)))
    moon_zoomed.convert()
    moon_zoomed_rect = moon_zoomed.get_rect()
    moon_zoomed_rect.center = zoom.center

    # phase surfaces
    phase_border = pygame.Rect(earth_rect.centerx + 5*earth_rect.width, earth_rect.centery - zoom_size/2, zoom_size, zoom_size)
    phases = []
    for i in range(1, 8+1):
        phase = pygame.image.load(resource_path("assets/earth_moon/phase_{}.png").format(i))
        phase = pygame.transform.scale(phase, (int(zoom_size*0.8),int(zoom_size*0.8)))
        phase.convert()
        phase_rect = phase.get_rect()
        phase_rect.center = phase_border.center
        phases.append((phase, phase_rect))
    phase_i = -1

    # zig-zag (separating sun from earth-moon system) surface
    zig_zag = pygame.image.load(resource_path("assets/earth_moon/zig-zag.png"))
    zig_zag = pygame.transform.scale(zig_zag, (50, height))
    zig_zag.convert()
    zig_zag_rect = zig_zag.get_rect()
    zig_zag_rect.center = (150, height/2)

    # sun surface
    sun = pygame.image.load(resource_path("assets/earth_moon/sun.png"))
    sun = pygame.transform.scale(sun, (int(sun_diameter*km_to_pixel), int(sun_diameter*km_to_pixel)))
    sun.convert()
    sun_rect = sun.get_rect()
    sun_rect.center = (-450, height/2)

    # text surfaces
    font = pygame.font.SysFont('Sans', 18)
    title = font.render('Lunar Phases:', True, WHITE)
    phase_title = font.render('Phase seen on Earth:', True, WHITE)
    zoom_title = font.render('Lunar surface:', True, WHITE)
    sun_title = font.render('The Sun:', True, WHITE)
    story = []
    with open(resource_path('assets/earth_moon/story.txt')) as file:
        story = [font.render(line.rstrip('\n'), True, WHITE) for line in file]
    story_i = 0
    progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE)
    stats = []
    stats.append('1 pixel = '+f'{int(1/km_to_pixel):,}'+' km')
    stats.append('Sun\'s diameter = '+f'{sun_diameter:,}'+' km')
    stats.append('Earth\'s diameter = '+f'{earth_diameter:,}'+' km')
    stats.append('Moon\'s diameter = '+f'{moon_diameter:,}'+' km')
    stats.append('Earth <-> Moon distance = '+f'{lunar_distance:,}'+' km')
    stats = [font.render(stat, True, WHITE) for stat in stats]
    guidance = font.render('ESC: exit.', True, WHITE)
    
    ### BEGIN ANIMATION ###

    # variables
    angle = 0
    speed = 20
    next_tick = 500
    radius = int(lunar_distance*km_to_pixel)

    # method that moves moon along circular path
    def move_coords(angle, radius):
        theta = math.radians(angle)
        return (earth_rect.centerx + radius * math.cos(theta), 
                earth_rect.centery + radius * math.sin(theta))

    # animation
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Was it the Escape key? If so, stop the loop.
                    return GameState.NEWGAME
                elif event.key == pygame.K_LEFT:
                    # move forward in story
                    if story_i > 0:
                        story_i -= 1
                        progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE)
                elif event.key == pygame.K_RIGHT:
                    # move backward in story
                    if story_i < len(story)-1:
                        story_i += 1
                        progress = font.render('{} of {}'.format(story_i+1, len(story)), True, WHITE)

        # move moon along orbit
        ticks = pygame.time.get_ticks() 
        if ticks > next_tick:
            next_tick += speed
            angle -= 1
            angle %= 360
            phase_i = len(phases) - (angle//45+1)
            moon_rect.center = move_coords(angle, radius)
            arrow_rect.center = moon_rect.left + arrow_rect.width, moon_rect.top
            zoom_border.center = arrow_rect.centerx + 2.5*arrow_rect.width, arrow_rect.centery
            zoom.center = zoom_border.center
            moon_zoomed_rect.center = zoom.center

        # determine current phase of moon
        phase_label = font.render(phase_dict[phase_i], True, WHITE)

        # display everything
        screen.blit(background, (0, 0))
        screen.blit(title, (width//2 - title.get_rect().width//2, title.get_rect().height))
        screen.blit(earth, earth_rect)
        pygame.draw.rect(screen, WHITE, phase_border, 2)
        screen.blit(*phases[phase_i])
        screen.blit(moon, moon_rect)
        screen.blit(arrow, arrow_rect)
        pygame.draw.rect(screen, WHITE, zoom_border, 2)
        pygame.draw.rect(screen, BLACK, zoom, 0)
        screen.blit(moon_zoomed, moon_zoomed_rect)
        screen.blit(phase_title, (phase_border.centerx - phase_title.get_rect().width//2, 
                                    phase_border.centery - phase_border.height))
        screen.blit(phase_label, (phase_border.centerx - phase_label.get_rect().width//2, 
                                    phase_border.centery + phase_border.height))
        screen.blit(zoom_title, (zoom_border.centerx - zoom_title.get_rect().width//2, 
                                    zoom_border.centery - zoom_border.height))
        screen.blit(zig_zag, zig_zag_rect)
        screen.blit(sun, sun_rect)
        screen.blit(sun_title, (10, sun_title.get_rect().height))
        screen.blit(story[story_i], ((width-story[story_i].get_rect().width)//2, height-2*story[story_i].get_rect().height))
        for stat_i, stat in enumerate(stats):
            screen.blit(stat, ((width-stat.get_rect().width-10, (stat_i+1)*stat.get_rect().height)))
        screen.blit(progress, ((width-progress.get_rect().width-10, height-2*progress.get_rect().height)))
        screen.blit(guidance, (10, height-2*guidance.get_rect().height))

        # update display
        pygame.display.update()
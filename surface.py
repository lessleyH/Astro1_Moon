import sys
import os
import pygame
from menu import GameState,resource_path
# get location of file
file_path = os.path.dirname(__file__)
if getattr(sys, 'assets', False):
    os.chdir(sys._MEIPASS)

# constants
size = width, height = 1040, 720 # pixels
km_to_pixel = 0.175 # real world units to computer screen units
moon_diameter = 1738.1*2 # km
WHITE = (255, 255, 255) # colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
button_radius = 15
def age_moon(screen):
    ### LOAD SURFACES ###

    # background surfaces
    space = pygame.image.load(resource_path("assets/moon_age/space.jpg"))
    space = pygame.transform.scale(space, size)
    space = space.convert()
    space_rect = space.get_rect()

    crater_counting = pygame.image.load(resource_path("assets/moon_age/crater_counting.png"))
    crater_counting = pygame.transform.scale(crater_counting, size)
    crater_counting = crater_counting.convert()
    crater_counting_rect = crater_counting.get_rect()

    highlands = pygame.image.load(resource_path("assets/moon_age/highlands.png"))
    highlands = pygame.transform.scale(highlands, size)
    highlands = highlands.convert()
    highlands_rect = highlands.get_rect()

    maria = pygame.image.load(resource_path("assets/moon_age/maria.png"))
    maria = pygame.transform.scale(maria, size)
    maria = maria.convert()
    maria_rect = maria.get_rect()

    poles = pygame.image.load(resource_path("assets/moon_age/poles.png"))
    poles = pygame.transform.scale(poles, size)
    poles = poles.convert()
    poles_rect = poles.get_rect()

    # near-side of moon surface
    near_side = pygame.image.load(resource_path("assets/moon_age/moon_near_side.png"))
    near_side = pygame.transform.scale(near_side, (int(moon_diameter*km_to_pixel), int(moon_diameter*km_to_pixel)))
    near_side = near_side.convert()
    near_side_rect = near_side.get_rect()
    near_side_rect.centerx, near_side_rect.centery = width//2, height//2

    # far-side of moon surface
    far_side = pygame.image.load(resource_path("assets/moon_age/moon_far_side.png"))
    far_side = pygame.transform.scale(far_side, (int(moon_diameter*km_to_pixel), int(moon_diameter*km_to_pixel)))
    far_side = far_side.convert()
    far_side_rect = far_side.get_rect()
    far_side_rect.centerx, far_side_rect.centery = width//2, height//2

    # text surfaces
    font = pygame.font.SysFont('Sans', 18)
    title = font.render('Lunar Surface:', True, WHITE)
    story, stats, topic = {}, {}, None
    with open(resource_path('assets/moon_age/story.txt')) as file:
        for line in file:
            if line.startswith('*'):
                topic = line[1:].rstrip('\n')
                story[topic] = []
                stats[topic] = font.render(topic+':', True, WHITE)
            else:
                story[topic].append(font.render(line.rstrip('\n'), True, WHITE))
    story_i, topic = 0, None
    guidance = font.render('SPACE: switch sides of Moon.   LEFT/RIGHT: for narration.   ESC: exit.   Click a colored dot to learn!', True, WHITE)
    progress = None
    side_label = {'near':font.render('Near Side:', True, WHITE), 'far':font.render('Far side:', True, WHITE)}

    ### BEGIN ANIMATION ###

    # variables
    current_side, current_side_rect = near_side, near_side_rect
    red_center = (current_side_rect.centerx-current_side_rect.width//4, current_side_rect.centery-current_side_rect.height//5)
    green_center = (current_side_rect.centerx, current_side_rect.centery-current_side_rect.height//4)
    blue_center = (current_side_rect.centerx, current_side_rect.centery+current_side_rect.height//2)
    orange_center = ((current_side_rect.centerx-current_side_rect.width//2)//2, current_side_rect.centery-current_side_rect.height//3)
    background, background_rect = space, space_rect

    # method that checks if mouse is close to a colored button
    def is_close(mouse_pos, button_pos):
        return button_pos[0]-button_radius < mouse_pos[0] < button_pos[0]+button_radius and \
                button_pos[1]-button_radius < mouse_pos[1] < button_pos[1]+button_radius

    # animation
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            # key press
            elif event.type == pygame.KEYDOWN:
                # during story
                if topic: 
                    if event.key == pygame.K_ESCAPE:
                        # exit story
                        topic = None
                        background, background_rect = space, space_rect
                    elif event.key == pygame.K_LEFT:
                        # move forward in story
                        if story_i > 0:
                            story_i -= 1
                            progress = font.render('{} of {}'.format(story_i+1, len(story[topic])), True, WHITE)
                    elif event.key == pygame.K_RIGHT:
                        # move backward in story
                        if story_i < len(story[topic])-1:
                            story_i += 1
                            progress = font.render('{} of {}'.format(story_i+1, len(story[topic])), True, WHITE)
                # main screen
                else:
                    # Was it the Escape key? If so, stop the loop.
                    if event.key == pygame.K_ESCAPE:
                        return GameState.NEWGAME
                    # switch side of Moon
                    elif event.key == pygame.K_SPACE:
                        if current_side is near_side:
                            current_side, current_side_rect = far_side, far_side_rect
                        else:
                            current_side, current_side_rect = near_side, far_side_rect
            # mouse press
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                # main screen
                if not topic:
                    # was a button clicked?
                    if current_side is near_side:
                        if is_close(pos, red_center):
                            topic, story_i = 'Maria', 0
                            background, background_rect = maria, maria_rect
                        elif is_close(pos, blue_center):
                            topic, story_i = 'Poles', 0
                            background, background_rect = poles, poles_rect
                    else:
                        if is_close(pos, green_center):
                            topic, story_i = 'Highlands', 0
                            background, background_rect = highlands, highlands_rect
                        elif is_close(pos, blue_center):
                            topic, story_i = 'Poles', 0
                            background, background_rect = poles, poles_rect
                    if is_close(pos, orange_center):
                        topic, story_i = 'Crater Counting', 0
                        background, background_rect = crater_counting, crater_counting_rect

        # increment progress metric
        if topic:
            progress = font.render('{} of {}'.format(story_i+1, len(story[topic])), True, WHITE)

        # display everything
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, BLACK, (width//2 - title.get_rect().width//2, title.get_rect().height, title.get_rect().width, title.get_rect().height))
        screen.blit(title, (width//2 - title.get_rect().width//2, title.get_rect().height))
        if topic:
            pygame.draw.rect(screen, BLACK, ((width-story[topic][story_i].get_rect().width)//2, height-2*story[topic][story_i].get_rect().height, story[topic][story_i].get_rect().width, story[topic][story_i].get_rect().height))
            screen.blit(story[topic][story_i], ((width-story[topic][story_i].get_rect().width)//2, height-2*story[topic][story_i].get_rect().height))
            screen.blit(progress, ((width-progress.get_rect().width-10, height-2*progress.get_rect().height)))
            pygame.draw.rect(screen, BLACK, (10, stats[topic].get_rect().height, stats[topic].get_rect().width, stats[topic].get_rect().height))
            screen.blit(stats[topic], (10, stats[topic].get_rect().height))
        else:
            screen.blit(current_side, current_side_rect)
            screen.blit(guidance, ((width-guidance.get_rect().width)//2, height-2*guidance.get_rect().height))
            if current_side is near_side:
                screen.blit(side_label['near'], (10, side_label['near'].get_rect().height))
                pygame.draw.circle(screen, RED, red_center, button_radius)
                pygame.draw.circle(screen, BLUE, blue_center, button_radius)
            elif current_side is far_side:
                screen.blit(side_label['far'], (10, side_label['far'].get_rect().height))
                pygame.draw.circle(screen, GREEN, green_center, button_radius)
                pygame.draw.circle(screen, BLUE, blue_center, button_radius)
            pygame.draw.circle(screen, ORANGE, orange_center, button_radius)

        # update display
        pygame.display.update()
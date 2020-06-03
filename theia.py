import os, sys
import pygame

# get location of file
file_path = os.path.dirname(__file__)

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

# initialize game
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Origins of the Moon')
font = pygame.font.SysFont(None, 24)

### LOAD SURFACES ###

# background surfaces
space = pygame.image.load(os.path.join(file_path, "assets/bg.jpg"))
space = pygame.transform.scale(space, size)
space = space.convert()
space_rect = space.get_rect()

#Proto Earth 
proto_earth = pygame.image.load(os.path.join(file_path, "assets/gih/protoEarth.jpg"))
proto_earth = pygame.transform.scale(proto_earth, size)
proto_earth = proto_earth.convert()
proto_earth_rect = proto_earth.get_rect()

#Theia First Impact 
theia_impact = pygame.image.load(os.path.join(file_path, "assets/gih/Theia_Impact.png"))
theia_impact = pygame.transform.scale(theia_impact, size)
theia_impact = theia_impact.convert()
theia_impact_rect = theia_impact.get_rect()

#Theia Impact Explostion
theia_2 = pygame.image.load(os.path.join(file_path, "assets/gih/Thea_impact3.jpg"))
theia_2= pygame.transform.scale(theia_2, size)
theia_2 = theia_2.convert()
theia_2_rect = theia_2.get_rect()

#Theia Impact Explostion
theia_3 = pygame.image.load(os.path.join(file_path, "assets/gih/ring_protoearth.jpg"))
theia_3= pygame.transform.scale(theia_3, size)
theia_3 = theia_3.convert()
theia_3_rect = theia_3.get_rect()

# Theia's actual size free floating png 
# theia_first = pygame.image.load(os.path.join(file_path, "assets/gih/MT.png"))
# theia_first  = pygame.transform.scale(theia_first, (int(mars_diameter*km_to_pixel), int(mars_diameter*km_to_pixel)))
# theia_first = theia_first.convert()
# theia_first_rect = theia_first.get_rect()
# theia_first_rect.centerx, theia_first_rect.centery = width//2, height//2

# Proto-Earth free floating png
# proto_earth_s = pygame.image.load(os.path.join(file_path, "assets/gih/proto-earth.png"))
# proto_earth_s = pygame.transform.scale(proto_earth_s, (int(proto_earth_diameter*km_to_pixel), int(proto_earth_diameter*km_to_pixel)))
# proto_earth_s = proto_earth_s.convert()
# proto_earth_s = proto_earth_s.get_rect()
# proto_earth_s_rect.centerx, proto_earth_s_rect.centery = width//2, height//2

# text surfaces
title = font.render('Giant Impact Hypothesis:', True, WHITE)
story, stats, topic = {}, {}, None
with open(os.path.join(file_path, 'assets/gih/story.txt')) as file:
    for line in file:
        if line.startswith('*'):
            topic = line[1:].rstrip('\n')
            story[topic] = []
            stats[topic] = font.render(topic+':', True, WHITE)
        else:
            story[topic].append(font.render(line.rstrip('\n'), True, WHITE))
story_i, topic = 0, None
guidance = font.render('LEFT/RIGHT: for narration,   ESC: exit,   Press the LEFT arrow to start. Have fun!', True, WHITE)
progress = None

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
            keydown = True
            # during story
            print("This is topic rn", topic)
            if topic: 
                if event.key == pygame.K_LEFT:
                    # move forward in story
                    print("Hi i am here")
                    if story_i > 0:
                        progress = font.render('{} of {}'.format(story_i+1, len(story[topic])), True, WHITE)
                        print("++++++++++++++++++all the way at the top", story[topic])
                    

                elif event.key == pygame.K_RIGHT:
                    # move backward in story
                    if story_i < len(story[topic])-1:
                        progress = font.render('{} of {}'.format(story_i+1, len(story[topic])), True, WHITE)
                    
                
                # exit story
                elif event.key == pygame.K_ESCAPE:
                    topic = None
                    background, background_rect = space, space_rect
                    #Go back to menu (?)
                
            
            # main screen
            if not topic and step == 0:
                topic, story_i = 'Space', 0
                background, background_rect = space, space_rect
                if(story_i == len(story[topic])-1):
                    step +=1


            print(step, " outsife if ")   

            if topic and step> 0 and story_i >0: 

                if step ==1: 
                    topic, story_i = 'Proto-Earth', 0
                    background, background_rect = proto_earth, proto_earth_rect

                if step ==2:
                    topic, story_i = 'Theia Impact', 0
                    background, background_rect = theia_impact, theia_impact_rect

                if step ==3:
                    topic, story_i = 'Theia Graze', 0
                    background, background_rect = theia_2, theia_2_rect

                if step ==4:
                    topic, story_i = 'Our Moon', 0
                    background, background_rect = theia_3, theia_3_rect
                

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
        screen.blit(guidance, (10, height-2*guidance.get_rect().height))
    # update display
    pygame.display.update()
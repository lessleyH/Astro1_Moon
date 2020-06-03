import pygame, sys 
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
size =(SCREEN_WIDTH ,SCREEN_HEIGHT)


def set_up(): 
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Origins of the Moon")
    win = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    return win, clock 


class Theia(pygame.sprite.Sprite): 
    def __init__(self):
        super(Theia, self).__init__()
        self.width = 200
        self.height = 150
        player_img = pygame.image.load("./assets/MT.png")
        player_img = pygame.transform.scale(player_img, (200, 150))
        self.surf = player_img.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = pygame.draw.circle(self.surf, (0,0,0), (10, 10), 5)
        self.wrap = False
        self.size = self.surf.get_size()
        self.bigger_img = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2))).convert()

    def update_size(self, value = 50):
        self.width += value
        self.height += value


def main():


    win, clock = set_up()

    background = pygame.image.load("./assets/bg.jpg")
    background = pygame.transform.scale(background, (size))
    background = background.convert()
    background_rect = background.get_rect()


    theia = Theia()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(theia)


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


        for entity in all_sprites:
            win.blit(entity.surf, entity.rect)

        
        win.blit(theia.surf, theia.rect)


        win.blit(theia.bigger_img,[100,100] )

        # Flip the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
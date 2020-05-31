import pygame
import random
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

#Stores information about a player
class Player:
    def __init__(self, current_level=1):
        super(Player,  self).__init__()
        self.surf = pygame.image.load("./assets/jeyL.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.current_level = current_level

def title_screen(screen):
    start_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 +100),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Start Game",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 +150),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit Game",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn)

    return game_loop(screen, buttons)


def play_level(screen, player):
    return_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, SCREEN_HEIGHT-50),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    formation_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, 260),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text=f"Formation of the Moon",
        action=GameState.NEXT_LEVEL,
    )

    earthMoon_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text=f"Earth Moon Systems",
        action=GameState.NEXT_LEVEL,
    )

    AgeMoon_btn = UIElement(
        center_position=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 +100),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text=f"Age of the Moon",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, formation_btn, earthMoon_btn, AgeMoon_btn)

    return game_loop(screen, buttons)


def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NEXT_LEVEL = 2
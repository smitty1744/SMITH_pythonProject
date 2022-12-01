import pygame
from mygame.sprite import Sprite

class Background(Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.surface.Surface((300, 300))


import pygame
# from pygame.sprite import Sprite
from PIL import Image

class Shooter:

    def __init__(self):
        self.original_shooter = pygame.image.load('images/shooter.png')
        self.shooter = self.original_shooter
        self.rect_a = self.shooter.get_rect()
        res_image_a = pygame.transform.scale(self.shooter, (50, 50))
        res_rect_a = res_image_a.get_rect(center=self.rect_a.center)
        self.shooter = res_image_a
        self.rect_a = res_rect_a

        self.x = float(self.rect_a.x)


    # def update(self):
    #     """Move the boy steadily to the left."""
    #     self.x += (self.settings.alien_speed * self.settings.fleet_direction)
    #     self.rect.x = self.x
    def update(self):
        pass

    def draw(self, screen):
        pass



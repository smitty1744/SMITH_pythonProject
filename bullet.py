import pygame
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):

    def __init__(self, tr_game):
        super().__init__()
        self.screen = tr_game.screen
        self.settings = tr_game.settings   # tr_game.screen
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        #Hava helped shooter position
        self.rect.center = tr_game.shooter.rect.center
        self.rect.y = tr_game.shooter.rect.y + 87

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

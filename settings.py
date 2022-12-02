# import sys
import pygame
# from pygame.locals import *


class Settings:

    def __init__(self):
        self.background = pygame.image.load('images/background.jpg')
        self.shooter = pygame.image.load('images/shooter_2.png')
        self.boy = pygame.image.load('images/boy_idle.png')
        self.boy_speed = 2
        self.boy_direction = -1
        self.boy_height = 50
        self.boy_width = 50
        self.boy_direction = 1
        self.shooter_width = 50
        self.shooter_height = 50
        self.shooter_speed = 2
        self.shooter_direction = -1
        self.bullet_speed = 6.0
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100000000000000000000000000

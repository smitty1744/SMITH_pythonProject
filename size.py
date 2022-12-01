import sys
import pygame
from pygame.locals import *

pygame.init()
# define the screen size
screen_width = 1200
screen_height = 500
# set the screen, upload, display the picture
screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("images/forest.png")
screen.blit(pygame.transform.scale(pic, (screen_width, screen_height)), (0, 0))
pygame.display.flip()
import pygame
import sys
from settings import Settings
from boy import Boy
from bullet import Bullet
from shooter import Shooter
# from mainscreen import Mainscreen
import sound_effects as se
from pygame.locals import *


class TrailRunner:

    def __init__(self):
        # initialize the game and create a screen object
        pygame.init()
        # create an object for the class Settings
        self.settings = Settings()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.pic = pygame.image.load("images/background.jpg")
        self.screen.blit(pygame.transform.scale(self.pic, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()
        pygame.display.set_caption('Trail Runner')

        # make a boy
        self.boy = Boy(self)
        self.boys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.shooter = Shooter(self)

    # -----------------------------------------------------------------------------------
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.boy.update()
            self._update_bullets()
            self.shooter.update()
            self._update_screen()
            se.background_sound.play()

    # -----------------------------------------------------------------------------------
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # -----------------------------------------------------------------------------------
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.boy.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.boy.moving_left = True
        elif event.key == pygame.K_UP:
            self.boy.jump = True
            print('jump')
        elif event.key == pygame.K_DOWN:
            self.boy.moving_down = True

    # ----------------------------------------------------
        elif event.key == pygame.K_d:
            self.shooter.moving_right = True
        elif event.key == pygame.K_a:
            self.shooter.moving_left = True
        elif event.key == pygame.K_w:
            self.shooter.jump = True
            print('jump')
        elif event.key == pygame.K_s:
            self.shooter.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            se.bullet_sound.play()
        elif event.key == pygame.K_q:
            sys.exit()

    # -----------------------------------------------------------------------------------
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.boy.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.boy.moving_left = False
        elif event.key == pygame.K_UP:
            self.boy.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.boy.moving_down = False
    # -----------------------------------------------------------------------
        elif event.key == pygame.K_d:
            self.shooter.moving_right = False
        elif event.key == pygame.K_a:
            self.shooter.moving_left = False
        elif event.key == pygame.K_w:
            self.shooter.moving_up = False
        elif event.key == pygame.K_s:
            self.shooter.moving_down = False

    # -----------------------------------------------------------------------------------
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        # se.bullet_sound.play()

    # -----------------------------------------------------------------------------------
    def _create_boy(self, boy_number, row_number):
        """Create an alien and place it in the row."""
        boy = Boy(self)
        # boy_width, boy_height = boy.rect_b.size
        self.boys.add(boy)

    # ---------------------------------------------------------------------------------------
    def _update_bullets(self):
        self.bullets.update()
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.boys, True, True)
        if not self.boy:
            self.bullets.empty()
        self._check_bullet_boy_collisions()

    # -----------------------------------------------------------------------------------
    def _check_bullet_boy_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.boys, True, True)
        if not self.boy:
            self.bullets.empty()
        # se.boy_sound.play()

    # -----------------------------------------------------------------------------------
    def _update_boy(self):
        self.boy.update()

    # -----------------------------------------------------------------------------------
    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.transform.scale(self.pic, (self.screen_width, self.screen_height)), (0, 0))
        self.boy.blitme()
        self.shooter.blitme()
        # self.screen.blit(self.settings.boy, (0, 0))
        # self.screen.blit(self.settings.shooter, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

# -----------------------------------------------------------------------------------


if __name__ == '__main__':
    # Make a game instance, and run the game.
    tr = TrailRunner()
    tr.run_game()

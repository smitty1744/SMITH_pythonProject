import pygame
import sys
from settings import Settings
from boy import Boy
from bullet import Bullet
from shooter import Shooter
import sound_effects as se


class TrailRunner:

    def __init__(self):
        # initialize the game and create a screen object
        pygame.init()
        # create an object for the class Settings
        self.settings = Settings()
        self.screen_width = 1200
        self.screen_height = 800

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.pic = pygame.image.load("images/background.jpg")
        self.pic = pygame.transform.scale(self.pic, (self.screen_width, self.screen_height))
        self.i = 0

        self.clock = pygame.time.Clock()
        self.base_font = pygame.font.Font(None, 70)
        self.user_text = 'Press Space to Start'
        self.ded_txt = '     Game Over!!!     '
        self.input_rect = pygame.Rect(358, 360, 380, 55)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
        self.active = False
        self.s = 0
        self.font = pygame.font.Font(None, 15)
        pygame.display.set_caption('Trail Runner')
        self.boy = Boy(self)
        self.boys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.shooter = Shooter(self)
        self.bullet_boy_collision = False
        se.background_sound.play()
        self.score_x = 80
        self.score_y = 80
        self.score = 0
        # if self.score > 50:
        #     self.ded_txt = '   Boy Wins!!!   '
        # if self.score == 50:
        #     self.ded_txt = '     Draw!!!     '
        # else:
        #     self.ded_txt = ' Shooter Wins!!! '

    # -----------------------------------------------------------------------------------
    def run_game(self):
        # Eli Watson helped with while True statement in order to update ending of game to allow it to exit out
        while True:
            if self.s == 0:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.s = 1
                            self.active = True
                        else:
                            pygame.quit()
                            sys.exit()
                self.screen.fill((255, 0, 0))
                if self.active:
                    self.color = self.color_active
                    self.s = 1
                else:
                    self.color = self.color_passive
                pygame.draw.rect(self.screen, self.color, self.input_rect)
                text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
                self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
                self.input_rect.w = max(100, text_surface.get_width() + 10)
                pygame.display.flip()
                self.clock.tick(60)
            elif self.s == 1:
                if self.boy.health > 0:
                    self._check_events()
                    self.boy.update()
                    self._update_bullets()
                    self.shooter.update()
                    self._update_screen()
                    self._check_bullet_boy_collisions()
                    self._check_shooter_boy_collisions()
                else:
                    self.screen.fill((255,0,0))
                    self._check_events()
                    pygame.draw.rect(self.screen, self.color, self.input_rect)
                    text_surface = self.base_font.render(self.ded_txt, True, (255, 255, 255))
                    self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
                    self.input_rect.w = max(100, text_surface.get_width() + 10)
                    self.clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                self.s = 1
                                self.active = True
                            else:
                                pygame.quit()
                                sys.exit()
                    pygame.display.flip()
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
        se.bullet_sound.play()
    # -----------------------------------------------------------------------------------

    def _create_boy(self):
        boy = Boy(self)
        self.boys.add(boy)
    # ---------------------------------------------------------------------------------------

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)
                self.score += 10
        self._check_bullet_boy_collisions()

    def _check_bullet_boy_collisions(self):
        self.boys.add(self.boy)
        collisions = pygame.sprite.groupcollide(self.bullets, self.boys, True, True)
        if not self.boy:
            self.bullets.empty()
        if collisions:
            self.boy.health -= 2
            self.score -= 5
            if self.score <= 0:
                self.score = 0
            print(f"Collision: boy health={self.boy.health}!!")
            se.boy_sound.play()

    def _check_shooter_boy_collisions(self):
        collisions = pygame.Rect.colliderect(
            self.shooter.rect, self.boy.rect)
        if collisions and self.boy.x <= self.shooter.x:
            self.shooter.x = 200
            self.boy.x = 800

    def show_score(self):
        score_text = self.base_font.render("SCORE: " +str(self.score), True, (255, 0, 0))
        self.screen.blit(score_text, (self.score_x, self.score_y))

    def _update_boy(self):
        self.boy.update()
        self._create_boy()
        self.boys.update()

    # -----------------------------------------------------------------------------------
    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.i -= self.boy.settings.boy_speed * .3
        self.screen.blit(self.pic, (self.i, 0))
        self.screen.blit(self.pic, (self.screen_width + self.i, 0))
        if self.i <= -self.screen_width:
            self.screen.blit(self.pic, (self.screen_width+self.i, 0))
            self.i = 0
        self.boy.blitme()
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.show_score()
        pygame.display.flip()
# -----------------------------------------------------------------------------------


if __name__ == '__main__':
    tr = TrailRunner()
    tr.run_game()


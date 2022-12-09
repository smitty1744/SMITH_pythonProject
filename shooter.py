import pygame


class Shooter:

    def __init__(self, tr_game):
        self.screen = tr_game.screen
        self.settings = tr_game.settings
        self.shooter = pygame.image.load("images/shooter.png")
        self.original_shooter = pygame.image.load('images/shooter.png')
        self.shooter = self.original_shooter
        self.rect_a = self.shooter.get_rect()

        self.jump    = False
        self.jump_itr = 0

        res_image_a = pygame.transform.scale(self.shooter, (150, 150))
        res_rect_a = res_image_a.get_rect(center=self.rect_a.center)
        self.shooter = res_image_a
        self.rect_a = res_rect_a

        self.image = self.shooter
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 538
        self.health = 100
        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False

    def update(self):
        if self.x >= 0:
            self.x -= self.settings.shooter_speed * .3
        if self.moving_right:
            self.x += self.settings.shooter_speed # * self.settings.boy_direction)

        # Jump sequence (go up 10px and come back down 10px).
        num_itr = 100
        if self.jump:
            if self.jump_itr < num_itr:
                self.y -= 3
                self.jump_itr += 1
            else:
                self.y += 3
                self.jump_itr += 1

            if self.jump_itr > 2*num_itr-1:
                self.jump = False
                self.jump_itr = 0

    def blitme(self):

        self.image = self.shooter
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)

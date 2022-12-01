import pygame


class Boy():

    def __init__(self, tr_game):
        super().__init__()
        self.screen = tr_game.screen
        self.settings = tr_game.settings
        self.healthy_image = pygame.image.load("images/boy_idle.png")
        self.light_damage_image = pygame.image.load("images/boy_hit.png")
        self.heavy_damage_image = pygame.image.load("images/boy_faint.png")
        # Hava Szarafinski resize image
        self.original_boy = pygame.image.load('images/boy_idle.png')
        self.boy = self.original_boy
        self.rect_b = self.boy.get_rect()

        self.jump    = False
        self.jump_itr = 0


        res_image_b = pygame.transform.scale(self.boy, (80, 80))
        res_rect_b = res_image_b.get_rect(center=self.rect_b.center)
        self.boy = res_image_b
        self.rect_b = res_rect_b

        # start healthy
        self.image = self.healthy_image
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 528
        self.health = 100
        self.x = int(self.rect.x)
        self.y = int(self.rect.y)


        # Moving variables.
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False

    def update(self):
        """Move the boy steadily to the left."""

        if self.moving_right:
            #cprint('Boy am moving right.')
            self.x += self.settings.boy_speed # * self.settings.boy_direction)


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

        self.health = 20
        self.image = self.healthy_image

        if self.health < 40:
            self.image = self.light_damage_image
        if self.health < 0:
            self.image = self.heavy_damage_image

        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect)

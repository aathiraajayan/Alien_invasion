import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # self.image = pygame.image.load('images/alien_ship.bmp')
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        ## start the position at the left top for all alien ship
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """drow alien in thir current location"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """ move the alien right """
        self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)


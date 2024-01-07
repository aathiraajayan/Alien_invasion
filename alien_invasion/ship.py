import pygame


class Ship:
    def __init__(self, screen, ai_settings) -> None:
        ## load screen
        self.screen = screen
        self.ai_settings = ai_settings
        
        ## load image data and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        ## start new ship at bottum center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        ##store decimal value for center
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship's position based on flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        ## drow the ship at its current location
        self.screen.blit(self.image, self.rect)

    def ship_center(self):
        ### drow ship at center
        self.rect.centerx = self.screen_rect.centerx

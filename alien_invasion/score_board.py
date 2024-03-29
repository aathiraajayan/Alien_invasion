import pygame
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    def __init__(self, screen, ai_settings, stats) -> None:
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.screen_rect = self.screen.get_rect()
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        ##Prepare intitial score image
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ship()

    def prep_score(self):
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        round_high_score = int(round(self.stats.high_score, -1))
        score_str = "{:,}".format(round_high_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_ship(self):
        self.ships = Group()
        for ship_count in range(self.stats.ship_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_count * ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)
        

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
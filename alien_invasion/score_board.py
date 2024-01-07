import pygame

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

    def prep_score(self):
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
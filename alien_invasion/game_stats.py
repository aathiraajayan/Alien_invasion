class GameStats():
    """ this calss stores the invasion game statistics"""
    def __init__(self, ai_settings) -> None:
        self.ai_settings = ai_settings
        self.reset_stats()
        # start game in inactive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """ Initialise statistics that can change during game """
        self.ship_left = self.ai_settings.ship_left
        self.score = 0
        self.level = 1






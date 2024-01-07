class Settings:
    """this class has all the settings for alien invasion game"""
    def __init__(self) -> None:
        ## screen settings
        self.screen_width = 1200
        self.screen_height = 700
        # self.screen_width = 1200
        # self.screen_height = 800
        self.bg_color = (230, 230, 230)


        ## bullet settings
        # self.bullet_width = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        ## alien settings
        self.fleet_drop_speed = 10

        ## ship statics
        self.ship_left = 3

        self.speedup_scale = 1.1
        self.initialise_dynamic_settings()

        self.score_scale = 1.5

    def initialise_dynamic_settings(self):
        self.ship_speed_factor = 1.5 # pixel
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 50

        self.fleet_direction = 1 ## 1 for right and and -1 for left

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale )
        

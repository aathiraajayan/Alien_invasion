import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():
    ## initialize game and create screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width,
        ai_settings.screen_height, 
        ))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    stats = GameStats(ai_settings)
    sb = ScoreBoard(screen, ai_settings, stats)

    play_button = Button(screen, 'Play')

    # starting main loop for the game
    while True:
        gf.check_events(ship, ai_settings, screen, sb, aliens, bullets, stats, play_button,)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, sb, stats, screen, aliens, bullets, ship)
            gf.update_aliens(ai_settings, sb, aliens, bullets, ship, screen, stats)
        gf.update_screen(ai_settings, sb, screen, ship, bullets, aliens, stats, play_button)

run_game()


#page - 341
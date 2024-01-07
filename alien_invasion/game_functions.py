import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_event(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullets(ship, ai_settings, screen, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        ai_settings.initialise_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.ship_center()


def check_events(ship, ai_settings, screen, aliens, bullets, stats, play_button,):
    ## watch for mouse and key board input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y)
            

def update_screen(ai_settings, sb, screen, ship, bullets, aliens, stats, play_button): 
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    sb.show_score()
    # alien.blitme()

    ## re draw bullets
    for bullet in bullets:
        bullet.draw_bullet()

    for alien in aliens:
        alien.blitme()

    if not stats.game_active:
        play_button.draw_button()

    ### most recent screen visible
    pygame.display.flip()


def update_bullets(ai_settings, sb, stats, screen, aliens, bullets, ship):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, sb, stats, screen, aliens, bullets, ship)


def check_bullet_alien_collision(ai_settings, sb, stats, screen, aliens, bullets, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)


def fire_bullets(ship, ai_settings, screen, bullets):
    """ fire the bullet if limit not exceed """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens, ship):
    """ created fleet of aliens """
    # no of aliens
    alien = Alien(screen, ai_settings)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

    
    # create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_add_alien(screen, ai_settings, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_add_alien(screen, ai_settings, aliens, alien_number, row_number):
    """ create and place the alien ship """
    alien = Alien(screen, ai_settings)
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens:
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """
    drop the fleet and change direction
    """
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens, bullets, ship, screen, stats):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    ### look for alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit !!!")
        ship_hit(ai_settings, screen, aliens,bullets, ship, stats)

    is_alien_hit_bottom = check_alien_hit_bottom(aliens)
    if is_alien_hit_bottom:
        ship_hit(ai_settings, screen, aliens,bullets, ship, stats)



def ship_hit(ai_settings, screen, aliens, bullets, ship, stats):
    """response to ship hit by alien"""
    if stats.ship_left > 0:
        stats.ship_left -= 1 

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.ship_center()

        ## pause
        sleep(0.5)
    else:
        stats.game_active = False 
        pygame.mouse.set_visible(True)




def check_alien_hit_bottom(aliens):
    for alien in aliens:
        if alien.check_bottom():
            return True
    return False


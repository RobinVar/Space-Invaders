import pygame
from pygame.sprite import Group
from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #initialize game and creating screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    ship = Ship(ai_settings,screen)
    # group to store bullets in
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # Starts the main loop of game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()
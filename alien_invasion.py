import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initl game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
     
    # create ship
    ship = Ship(ai_settings, screen)
    #create bullet
    bullets = Group()
     
    # Start game
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # delect bullet
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)
        
       
run_game()
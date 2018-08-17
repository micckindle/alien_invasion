import pygame

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
     
    # Start game
    while True:
        
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
       
run_game()
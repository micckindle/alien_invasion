import sys
import pygame

from settings import Settings

def run_game():
    # Initl game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
          
    # Start game
    while True:
        
        # keyboard and mouse thing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # draw screen
        screen.fill(ai_settings.bg_color)
        
        # screen visible
        pygame.display.flip()
        
    
        
run_game()
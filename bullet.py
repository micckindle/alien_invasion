import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''manage a bullet'''
    
    def __init__(self, ai_settings, screen, ship):
        '''create a bullet'''
        super(Bullet, self).__init__()
        self.screen = screen
        
        # create bullet at (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # store bullet 
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        ''' move bullet '''
        #update bullet 
        self.y -= self.speed_factor
        #update bullet rect
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
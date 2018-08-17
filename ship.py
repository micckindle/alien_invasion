import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        '''init ship and setting location'''
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # set ship locaiton
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        
        # set ship to bottom
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        
        # move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False  
        self.moving_down = False        
    
    def update(self):
        ''' move the ship'''        
        # update center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            #print(str(self.moving_right) + "," +str(self.rect.right))
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            #print(str(self.moving_left) + "," +str(self.rect.left))
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
            #print(str(self.centery) + "," +str(self.rect.top))
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            #print(str(self.moving_down) + "," +str(self.rect.bottom))
            
        # update rect
        self.rect.centerx = self.center
        self.rect.centery = self.centery
    
    def blitme(self):
        '''draw a ship'''
        self.screen.blit(self.image, self.rect)
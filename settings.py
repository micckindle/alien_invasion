class Settings():
    ''' save alien invasion setting'''
    
    def __init__(self):
        ''' init all game setting'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.5
        
        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 162, 233
        
        
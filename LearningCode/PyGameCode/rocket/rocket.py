""" rocket class : put an image on the screen and allow it to move around """
import pygame

class Rocket:
    def __init__(self,ai_game):
        """ initilaize rocket settings """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load shp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center    #center of screen 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 1.0
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """ update rocket position """
        if self.moving_right and self.rect.right < self.screen_rect.right:          
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.top > 2:  # leave margin
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:     
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """draw rocket at current location"""
        self.screen.blit(self.image, self.rect)
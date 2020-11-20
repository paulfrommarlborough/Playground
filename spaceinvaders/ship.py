import pygame

class Ship:
    """ class for our ship """
    def __init__(self, ai_game):
        """ init ship. Set starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load shp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)
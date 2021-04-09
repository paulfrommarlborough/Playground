import pygame

""" settings class for the flyrocket app """
class Settings:
    def __init__(self):
        """ initilaize settings """
        self.key_name = "undefined key"
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
#        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        self.white = (255, 255, 255) 
        self.green = (0, 255, 0) 
        self.blue = (0, 0, 128)
       

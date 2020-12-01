""" put ship in center of screen and allow it to move left, right, up, down,     30-nov-2020 """
import sys
import pygame
from settings import Settings
from rocket import Rocket


class FlyRocket:
    
    def __init__(self):
        """ init the fly rocket app """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Fly Rocket")
        self.rocket = Rocket(self)

    def event_key_down(self,event):
        """ key press event handler"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True           
        elif event.key == pygame.K_q:
            print("thanks for flying, see you later...")
            sys.exit()

    def event_key_up(self,event):
        """ key release event handler"""
        if event.key == pygame.K_LEFT: 
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT: 
            self.rocket.moving_right = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        
    def check_events(self):
        """ main event handler"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.event_key_down(event)
            elif event.type == pygame.KEYUP:
                self.event_key_up(event)
                              
    def update_screen(self):
        """ Redraw the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_color)        
        self.rocket.blitme()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()
            self.rocket.update()
            self.update_screen()
            # Make the most recently drawn screen visible. 
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance, and run the game.
    ai = FlyRocket()
    ai.run_game()


import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ spaceinvaders_main.py  stub """
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def event_key_down(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def event_key_up(self,event):
        if event.key == pygame.K_LEFT: 
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT: 
            self.ship.moving_right = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.event_key_down(event)
            elif event.type == pygame.KEYUP:
                self.event_key_up(event)
                
               
    def update_screen(self):
            # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
            
        self.ship.blitme()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()

            self.ship.update()

            self.update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

""" main """
import sys
import pygame
from settings import Settings
from rocket import Rocket


class FlyRocket:
    
    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Fly Rocket")
        self.rocket = Rocket(self)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = FlyRocket()
    ai.run_game()


""" spaceinvaders_main.py  stub """
import sys
import pygame

class AlienInvasion:
    """ overal class """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("space invaders")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == "__main__":
    print(f"space invaders sub")
    ai = AlienInvasion()
    print(f"run game")
    ai.run_game()
    print(f"done")

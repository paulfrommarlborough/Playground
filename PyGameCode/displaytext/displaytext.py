""" display key press  in pygame    30-nov-2020 """
import sys
import pygame
from settings import Settings

class DisplayText:
    
    def __init__(self):
        """ init the fly rocket app """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("display text")
    
    def event_key_down(self,event):
        """ key press event handler"""
       
        self.settings.key_name = str(event.key)

        if event.key == pygame.K_q:
            print("thanks, see you later...")
            sys.exit()

        
    def check_events(self):
        """ main event handler"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.event_key_down(event)
                              
    def update_screen(self):
        """ Redraw the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_color)   
       
        text = self.settings.font.render(self.settings.key_name, True, self.settings.green, self.settings.blue)  
        textRect = text.get_rect() 
        textRect.center = (200, 50) 
        self.screen.blit(text, textRect) 
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()
            self.update_screen()
            # Make the most recently drawn screen visible. 
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance, and run the game.
    ai = DisplayText()
    ai.run_game()
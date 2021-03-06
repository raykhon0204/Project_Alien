import sys 
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
    ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen)
    #start the main loop for the game
    while True:

        #watch for keyboard and mouse events
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)

        ship.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

run_game()


import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen # Assigning the screen to an attribute of Ship
        self.screen_rect = ai_game.screen.get_rect() # Getting the screen's rect attribute
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # Loading the image and assigning it to self.image
        self.rect = self.image.get_rect() # Getting the image's rect attribute
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # Setting the ship's rect's midbottom attribute to match the screen's midbottom attribute
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # Drawing the image to the screen at the position specified by self.rect
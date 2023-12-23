import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen # Assigning the screen to an attribute of Ship
        self.settings = ai_game.settings # Assigning the settings to an attribute of Ship
        self.screen_rect = ai_game.screen.get_rect() # Getting the screen's rect attribute
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') # Loading the image and assigning it to self.image
        self.rect = self.image.get_rect() # Getting the image's rect attribute
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # Setting the ship's rect's midbottom attribute to match the screen's midbottom attribute

        # Store a float value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down= False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: # Checking if the ship's right attribute is less than the screen's right attribute
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # Drawing the image to the screen at the position specified by self.rect
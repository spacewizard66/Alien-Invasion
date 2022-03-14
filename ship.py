import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A Class to Manage Ship"""

    def __init__(self, ai_game):
        """Initialize Ship, Set Starting Position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load Image and Get its Rectangle
        self.image = pygame.image.load('images\ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start Each New Ship at the Bottom of the Screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store Decimal Value for Ship's Horizontal Position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update Ship's Position Based on Movement Flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the Ship at its Current Location"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
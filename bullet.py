
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to Manage Bullets Fired from Ship"""

    def __init__(self, ai_game):
        """Create Bullet Object at Ship's Current Position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a Bullet Rect at (0, 0) then Set Correct Position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store Bullet's Position as Decimal Value
        self.y = float(self.rect.y)


    def update(self):
        """Move the Bullet Up the Screen"""
        
        # Update Decimal Position of Bullet
        self.y -= self.settings.bullet_speed
        # Update Rect Position
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the Bullet to the Screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
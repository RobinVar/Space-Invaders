import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Manage bullets fired form ship"""
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect @ 0,0 and then adjusts
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet as float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
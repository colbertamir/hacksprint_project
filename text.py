import pygame
from config import *

class Text(pygame.sprite.Sprite):
    def __init__(self, center_pos, text_content, font_size, bg_color, text_color):
        super().__init__()

        self.image = make_surface(text_content, font_size, text_color, bg_color)
        self.rect = self.image.get_rect(center = center_pos)
    
    
    def update(self, mouse_pos, clicked):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
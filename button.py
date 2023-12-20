import pygame
from config import *

class Button(pygame.sprite.Sprite):
    def __init__(self, center_pos, text_content, font_size, bg_color, text_color, highlight_color, action):
        super().__init__()

        self.hover = False

        self.action = action

        default_image = make_surface(text_content, font_size, text_color, bg_color)

        highlighted_image = make_surface(text_content, font_size * 1.2, highlight_color, bg_color)

        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(center = center_pos), highlighted_image.get_rect(center = center_pos)]
    
    @property
    def image(self):
        return self.images[1] if self.hover else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.hover else self.rects[0]
    
    def update(self, mouse_pos, clicked):
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
            if clicked:
                return self.action
        else:
            self.hover = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
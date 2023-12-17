import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 20)
        self.color = (255, 0, 0)
import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 
    # method to update position of the sprite to the same as the mouse position
    def update(self, new_x, pos_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
           self.rect.x -= 5 # move left
        if keys[pygame.K_RIGHT]:
           self.rect.x += 5 # move right
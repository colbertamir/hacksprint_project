import pygame, sys, random
from constants import *

class Wizard(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = [self.pos_x, self.pos_y]
        self.hitbox = pygame.Rect(self.pos_x + 15, self.pos_y + 45, 65, 65)
        self.dx = 0.5
        self.dy = 0.75
        self.health = 10

        # Set up the direction change variables
        self.change_direction_time = 0
    
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        
    # method to update position of the sprite to the same as the mouse position
    def update(self, current_time):

    # If it's time to change direction, reverse dx and dy
        if current_time - self.change_direction_time > random.randrange(300, 1000):
            self.dy *= -1
            self.change_direction_time = current_time
        if self.rect.left < 50 or self.rect.right > SCREEN_WIDTH - 50:
            self.dx *= -1
            self.pos_x += self.dx
        if self.rect.top < 25 or self.rect.bottom > SCREEN_HEIGHT - 400:
            self.dy *= -1
            self.pos_y += self.dy
         # Update the rectangle's position
        self.pos_x += self.dx
        self.pos_y += self.dy
        self.rect.center = (self.pos_x, self.pos_y)
        self.hitbox.center = (self.pos_x + 15, self.pos_y + 45)
    

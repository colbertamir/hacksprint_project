import pygame, sys
from player_projectile import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.gunshot = pygame.mixer.Sound("shoot.wav")
        self.hitbox = pygame.Rect(pos_x + 15, pos_y + 45, 50, 50)

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    # method to update position of the sprite to the same as the mouse position
    def update(self, new_x, pos_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
           self.rect.x -= 5 # move left
        if keys[pygame.K_RIGHT]:
           self.rect.x += 5 # move right
        self.hitbox.x = self.rect.x + 15
        self.hitbox.y = self.rect.y + 45

        # KEEP PLAYER ON SCREEN
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
    
        # method for shots sound
    def shoot(self):
        self.gunshot.play()
    
    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.top, "candycane3.png")
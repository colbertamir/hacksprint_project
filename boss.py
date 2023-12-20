import pygame, sys, random
from constants import *
from boss_projectile import Ice

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.penganimation = False
        self.sprites = []
        self.sprites.append(pygame.image.load(BOSS_IMGS[0]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[1]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[2]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[3]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[4]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[5]))
        self.sprites.append(pygame.image.load(BOSS_IMGS[6]))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = [self.pos_x, self.pos_y]
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, 100, 100)
        self.dx = 0.5
        self.dy = 0.75
        self.health = 35

        # Set up the direction change variables
        self.change_direction_time = 0
    
    def attack(self):
        self.penganimation = True
    
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        
    # method to update position of the sprite to the same as the mouse position
    def update(self, current_time, speed):
        if self.penganimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.penganimation = False
                
            self.image = self.sprites[int(self.current_sprite)]

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
        self.hitbox.center = (self.pos_x, self.pos_y)

    def create_ice(self):
        return Ice(self.rect.centerx, self.rect.centery, "assets/ice.png")
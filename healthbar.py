import pygame, sys
from constants import *

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(HP_BAR[0]) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.gunshot = pygame.mixer.Sound("assets/shoot.wav")
        self.hitbox = pygame.Rect(pos_x + 15, pos_y + 45, 75, 90)
        self.health = 12

    def update(self, health):
        if health == 12:
            self.image = pygame.image.load(HP_BAR[0])
        elif health == 11 or health == 10:
            self.image = pygame.image.load(HP_BAR[1])
        elif health == 9 or health == 8:
            self.image = pygame.image.load(HP_BAR[2])
        elif health == 7 or health == 6:
            self.image = pygame.image.load(HP_BAR[3])
        elif health <= 5 and health >= 1:
            self.image = pygame.image.load(HP_BAR[4])
        elif health == 0:
            self.image = pygame.image.load(HP_BAR[5])


class BossHealthBar(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(BOSS_HP_BAR[0]) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.gunshot = pygame.mixer.Sound("assets/shoot.wav")
        self.hitbox = pygame.Rect(pos_x + 15, pos_y + 45, 75, 90)
        self.health = 35

    def update(self, health):
        if health <= 35 and health >= 29:
            self.image = pygame.image.load(BOSS_HP_BAR[0])
        if health <= 28 and health >= 22:
            self.image = pygame.image.load(BOSS_HP_BAR[1])
        elif health <= 21 and health >= 15:
            self.image = pygame.image.load(BOSS_HP_BAR[2])
        elif health <= 14 and health >= 8:
            self.image = pygame.image.load(BOSS_HP_BAR[3])
        elif health <= 7 and health >= 1:
            self.image = pygame.image.load(BOSS_HP_BAR[4])
        elif health == 0:
            self.image = pygame.image.load(BOSS_HP_BAR[5])
        

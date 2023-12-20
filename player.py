import pygame, sys
from player_projectile import Bullet
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.treeanimation = False

        # LOAD IMAGES FOR ANIMATIOM
        self.sprites = []
        self.sprites.append(pygame.image.load(PLAYER_IMGS[0]))
        self.sprites.append(pygame.image.load(PLAYER_IMGS[1]))
        self.sprites.append(pygame.image.load(PLAYER_IMGS[2]))
        self.sprites.append(pygame.image.load(PLAYER_IMGS[3]))
        self.sprites.append(pygame.image.load(PLAYER_IMGS[4]))
        self.sprites.append(pygame.image.load(PLAYER_IMGS[5]))
        
        # START ON FIRST IMAGE
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # GET RECTANGLE AND SET POSITION
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        # LOAD SHOOT SOUND
        self.gunshot = pygame.mixer.Sound(PLAYER_SHOOT)

        # CREATE HITBOX
        self.hitbox = pygame.Rect(pos_x + 15, pos_y + 20, 75, 90)

        # SET HEALTH AND LIVES
        self.health = 12
        self.lives = 2
    
    # START ANIMATION
    def animate(self):
        self.treeanimation = True

    # DRAW HITBOX
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    # UPDATE IMAGE AND POSITION OF PLAYER
    def update(self, new_x, pos_y, speed):
        if self.treeanimation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.treeanimation = False
                
            self.image = self.sprites[int(self.current_sprite)]
        
        # RETREIVE PRESSED KEYS
        keys = pygame.key.get_pressed()

        # CHECK IF PLAYER NEEDS TO MOVE LEFT OR RIGHT
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
           self.rect.x -= 10 # move left
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           self.rect.x += 10 # move right
        
        # SET POSITION OF HITBOX
        self.hitbox.x = self.rect.x + 15
        self.hitbox.y = self.rect.y + 20

        # KEEP PLAYER ON SCREEN
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
    
    # METHOD FOR SHOT SOUND
    def shoot(self):
        self.gunshot.play()
    
    # CREATE BULLET
    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.top, PLAYER_PROJECTILE)


class Lives(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("assets/treesicon1.png") # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    
    def update(self, lives):
        if lives == 2:
            self.image = pygame.image.load("assets/treesicon1.png")
        elif lives == 1:
            self.image = pygame.image.load("assets/treesicon2.png")
        elif lives == 0:
            self.kill()

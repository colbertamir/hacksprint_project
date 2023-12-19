import pygame
from constants import *

class Ice(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        
        # SET POSITION AND SPEED
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.speed = 10

        # LOAD IMAGE
        self.image = pygame.image.load(picture_path) # load the sprite image

        # LOAD SOUND
        self.jingle = pygame.mixer.Sound(BOSS_SHOOT)

        # WIDTH AND HEIGHT
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # SET IMAGE AT POSITION
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))

        # MAKE HITBOX
        self.hitbox = pygame.Rect(pos_x + 15, pos_y + 30, 25, 45)
    
    # METHOD TO PLAY SOUND
    def jangle(self):
        self.jingle.play()
    
    # DRAW HITBOX
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    # UPDATE POSITION OF PROJECTILE
    def update(self):
        self.rect.y += self.speed
        self.speed -= 0.005

        # KILL PROJECTILE IF GONE PAST SCREEN
        if self.rect.y >= SCREEN_HEIGHT + 200:
            self.kill()

        # MOVE POSITION OF HITBOX
        self.hitbox.x = self.rect.x + 15
        self.hitbox.y = self.rect.y + 30
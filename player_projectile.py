import pygame, sys

screen_height = 900

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.jingle = pygame.mixer.Sound("bells.mp3")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        self.hitbox = pygame.Rect(pos_x + 35, pos_y + 30, 25, 45)
    
    def jangle(self):
        self.jingle.play()
    
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    def update(self):
        self.rect.y -= 15
        if self.rect.y >= screen_height + 200:
            self.kill()
        self.hitbox.x = self.rect.x + 35
        self.hitbox.y = self.rect.y + 30
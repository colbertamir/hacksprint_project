import pygame, sys, random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.gunshot = pygame.mixer.Sound("shoot.wav")


    # method to update position of the sprite to the same as the mouse position
    def update(self, new_x, pos_y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
           self.rect.x -= 5 # move left
        if keys[pygame.K_RIGHT]:
           self.rect.x += 5 # move right
        
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
    
    def update(self):
        self.rect.y -= 15

        if self.rect.y >= screen_height + 200:
            self.kill()

class Wizard(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 
    # method to update position of the sprite to the same as the mouse position
    def update(self):
        direction = random.choice(['left', 'right', 'up', 'down'])

        if direction == 'left':
            self.rect.x -= 5
        elif direction == 'right':
            self.rect.x += 5
        elif direction == 'up':
            self.rect.y += 5
        elif direction == 'down':
            self.rect.y += 5

# GENERAL SETUP
pygame.init()
clock = pygame.time.Clock()

# GAME SCREEN
screen_width = 800
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("bg.png") # load background image
pygame.mouse.set_visible(False) # make mouse invisible

# PLAYER INFO
playerX = 400
playerY = 800
change_pos = 0

wizardX = 400
wizardY = 200

player = Player(playerX, playerY, "tree2.png") # create instance of the sprite
player_group = pygame.sprite.Group() # create group to add sprites to
player_group.add(player) # add sprite to a group so it can be created and visible on the screen

bullet_group = pygame.sprite.Group()

wizard = Wizard(wizardX, wizardY, "ice_king.png")
wizard_group = pygame.sprite.Group()
wizard_group.add(wizard)

# MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
        
        if event.type == pygame.MOUSEBUTTONDOWN: # play sound when mouse is clicked
            player.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0)) # add background to screen
    player_group.draw(screen) # create all sprites from specific group
    wizard_group.draw(screen)
    player_group.update(playerX, playerY) # update the position of the all sprites in specific group
    bullet_group.draw(screen)
    bullet_group.update()
    wizard_group.update()
    clock.tick(120)
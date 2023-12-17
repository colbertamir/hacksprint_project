import pygame, sys, random
# Constants to use in the other files

# GAME SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
BACKGROUND = "bg2.png"

# PLAYER INFO
PLAYER_X = 400
PLAYER_Y = 800
PLAYER_IMAGE = "tree4.png"

# WIZARD INFO
WIZARD_X = 400
WIZARD_Y = 200
WIZARD_IMAGE = "ice_king.png"

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
    


# GENERAL SETUP
pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load(BACKGROUND) # load background image
pygame.mouse.set_visible(False) # make mouse invisible


player = Player(PLAYER_X, PLAYER_Y, PLAYER_IMAGE) # create instance of the sprite
player_group = pygame.sprite.Group() # create group to add sprites to
player_group.add(player) # add sprite to a group so it can be created and visible on the screen

bullet_group = pygame.sprite.Group()

wizard = Wizard(WIZARD_X, WIZARD_Y, WIZARD_IMAGE)
wizard_group = pygame.sprite.Group()
wizard_group.add(wizard)

bullets = []

# MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # play sound when mouse is clicked
                bullets.append(player.create_bullet())
                for bullet in bullets:
                    bullet_group.add(bullet)
                player.shoot()
        for bullet in bullets:
            if bullet.hitbox.colliderect(wizard.hitbox):
                if wizard.health <= 0:
                    wizard.kill()
                print(wizard.health)
                wizard.health -= 1
                bullet.jangle()
                print("hit")

        current_time = pygame.time.get_ticks()

    
    # RENDER DISPLAY
    pygame.display.flip()
    screen.blit(background, (0, 0)) # add background to screen

    # RENDER IMAGES
    player_group.draw(screen) # create all sprites from specific group
    wizard_group.draw(screen)
    bullet_group.draw(screen)

    # UPDATE SPRITES
    player_group.update(PLAYER_X, PLAYER_Y) # update the position of the all sprites in specific group
    bullet_group.update()
    wizard_group.update(current_time)

    # HIT BOXES
    player.draw(screen)
    wizard.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    clock.tick(120)
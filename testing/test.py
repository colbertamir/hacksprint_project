import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path) # load the sprite image
        self.rect = self.image.get_rect()
    # method to update position of the sprite to the same as the mouse position
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# GENERAL SETUP
pygame.init()
clock = pygame.time.Clock()

# GAME SCREEN
screen_width = 800
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("bg.png") # load background image
pygame.mouse.set_visible(False) # make mouse invisible

crosshair = Crosshair("tree.png") # create instance of the sprite
crosshair_group = pygame.sprite.Group() # create group to add sprites to
crosshair_group.add(crosshair) # add sprite to a group so it can be created and visible on the screen

# MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    screen.blit(background, (0, 0)) # add background to screen
    crosshair_group.draw(screen) # create all sprites from specific group
    crosshair_group.update() # update the position of the all sprites in specific group
    clock.tick(60)
import pygame, sys
from player import Player
from wizard import Wizard
from player_projectile import Bullet
from constants import *

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


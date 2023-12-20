import pygame, sys
from player import Player, Lives
from boss import Boss
from healthbar import HealthBar, BossHealthBar
from player_projectile import Bullet
from constants import *

# GENERAL SETUP
pygame.init()
pygame.display.set_caption('Iceicle: A Winter Adventure')
clock = pygame.time.Clock()

# CREATE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load(BACKGROUND) # load background image
pygame.mouse.set_visible(True) # make mouse invisible
pygame.time.set_timer(FIRE_EVENT, 250)

# CREATE PLAYER
player = Player(PLAYER_X, PLAYER_Y) # create instance of the sprite
player_group = pygame.sprite.Group() # create group to add sprites to
player_group.add(player) # add sprite to a group so it can be created and visible on the screen

# CREATE BULLET GROUP
bullet_group = pygame.sprite.Group()

# CREATE BOSS
boss = Boss(BOSS_X, BOSS_Y, BOSS_IMAGE)
boss_group = pygame.sprite.Group()
boss_group.add(boss)

# CREATE ICE GROUP
ice_group = pygame.sprite.Group()

# CREATE HEALTHBARS
healthbar = HealthBar(75, 880)
healthbar_group = pygame.sprite.Group()
healthbar_group.add(healthbar)

boss_healthbar = BossHealthBar(720, 30)
bosshealthbar_group = pygame.sprite.Group()
bosshealthbar_group.add(boss_healthbar)

lives = Lives(735, 860)
lives_group = pygame.sprite.Group()
lives_group.add(lives)

# FUNCTION TO MAKE A SURFACE
def make_surface(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.Font("assets/8bit.ttf", font_size)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

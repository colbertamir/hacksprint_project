# Constants to use in the other files
import pygame
from enum import Enum

# COLORS
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# GAME SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
BACKGROUND = "assets/bg2.png"

# PLAYER INFO
PLAYER_X = 400
PLAYER_Y = 800
PLAYER_IMAGE = "assets/lighttree1.png"

# WIZARD INFO
BOSS_X = 400
BOSS_Y = 200
BOSS_IMAGE = "assets/peng0.png"

# PROJECTILES
PLAYER_PROJECTILE = "assets/candycane3.png"

# ICE INFO
FIRE_EVENT= pygame.USEREVENT + 1

TIMER_EVENT = pygame.USEREVENT + 1

# GAME_EVENT
class GameEvent(Enum):
    TITLESCREEN = 0
    STARTGAME = 1
    STARTOVER = 2
    STATIC = 3
    GAMEOVER = 4

# HP
HP_BAR = ["assets/hp0.png",
          "assets/hp1.png",
          "assets/hp2.png",
          "assets/hp3.png",
          "assets/hp4.png",
          "assets/hp5.png"]

# HP
BOSS_HP_BAR = ["assets/boss_hp0.png",
          "assets/boss_hp1.png",
          "assets/boss_hp2.png",
          "assets/boss_hp3.png",
          "assets/boss_hp4.png",
          "assets/boss_hp5.png"]

# PLAYER

PLAYER_IMGS = ['assets/lighttree1.png',
                 'assets/lighttree2.png',
                 'assets/lighttree3.png',
                 'assets/lighttree4.png',
                 'assets/lighttree5.png',
                 'assets/lighttree6.png']

BOSS_IMGS = ['assets/peng0.png',
             'assets/peng1.png',
             'assets/peng2.png',
             'assets/peng3.png',
             'assets/peng4.png',
             'assets/peng5.png',
             'assets/peng6.png']

# SHOOT SOUNDS
PLAYER_SHOOT = "assets/shoot.wav"
BOSS_SHOOT = "assets/bells.mp3"

import pygame, sys
from constants import *
from config import *
from loops import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 900))
    game_state = GameEvent.TITLESCREEN

    running = True
    while running:
        if game_state == GameEvent.TITLESCREEN:
            game_state = title_screen(screen)

        if game_state == GameEvent.STARTGAME:
            game_state = game_loop(screen)
        
        if game_state == GameEvent.STARTOVER:
            player.lives = 2
            game_state = game_loop(screen)
        
        if game_state == GameEvent.GAMEOVER:
            game_state = game_over(screen)
main()
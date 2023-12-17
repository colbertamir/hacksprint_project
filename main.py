import pygame, sys
from player import Player
from wizard import Wizard
from player_projectile import Bullet
from constants import *
from config import *

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
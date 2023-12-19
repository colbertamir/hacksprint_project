import pygame
from constants import *
from button import Button
from text import Text
from pygame.sprite import RenderUpdates
from config import *
import random


def title_screen(screen):

    title1 = Text(
        center_pos = (210, 75),
        font_size = 45,
        bg_color = None,
        text_color = (23, 37, 64),
        text_content = 'ICEICLE'
    )

    title2 = Text(
        center_pos = (210, 130),
        font_size = 20,
        bg_color = None,
        text_color = (219, 243, 254),
        text_content = 'a winter adventure'
    )


    start_button = Button(
        center_pos = (205, 230),
        font_size = 30,
        bg_color = None,
        text_color = (149, 23, 23),
        text_content = 'START',
        action = GameEvent.STARTGAME,
    )

    buttons = RenderUpdates(title1, title2, start_button)

    running = True
    while running:
        mouse_up = False
        for event in pygame.event.get():

                    # CHECK IF USER EXITED
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
        
        pygame.display.flip()
        screen.blit(pygame.image.load("assets/pixelsnow.png"), (0, -200)) # add background to screen
        button.draw(screen)
        title1.draw(screen)
        title2.draw(screen)
        pygame.display.flip()


def game_loop(screen):

    # MAKE MOUSE INVISIBLE WHILE PLAYING
    pygame.mouse.set_visible(False)

    # RESET HEALTH
    player.health = 12
    boss.health = 35

    # RESET LISTS
    bullets = []
    ices = []

    #EMPTY GROUPS
    ice_group.empty()
    bullet_group.empty()

    # PLAYER READY STATUS
    ready = False

    # RESENT FIRE COUNT FOR BOSS
    fire_count = 0


# MAIN GAME LOOP
    while True:

        # LOOP THROUGH ALL EVENTS
        for event in pygame.event.get():

            # CHECK IF USER EXITED
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # CHECK IF USER SHOT PROJECTILE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.health > 0:
                    bullets.append(player.create_bullet())
                    for bullet in bullets:
                        bullet_group.add(bullet)
                    player.shoot()
            
            # CHECK IF PLAYER IS READY TO START FIGHTING
            if event.type == pygame.KEYDOWN:
                ready = True
            
            # FIRING PATTERN FOR BOSS
            fc_num = random.randrange(7, 11)

            if fire_count <= fc_num:
                if ready and event.type == FIRE_EVENT and boss.health > 0 and player.health > 0:
                    if fire_count < random.randrange(3, 6):
                        boss.attack()
                        ices.append(boss.create_ice())
                        for ice in ices:
                            ice_group.add(ice)
                    fire_count += 1
                    if fire_count > fc_num:
                        fire_count = 0

            # CHECK COLLISION OF PLAYER PROJECTILE AND BOSS
            if boss.health >= 0:
                for bullet in bullets:
                    if bullet.hitbox.colliderect(boss.hitbox):
                        bullet.jangle()
                        bullet.kill()
                        boss.health -= 1
                        print(boss.health)
                        print("BOSS was hit")
                        bullets.remove(bullet)

            # CHECK COLLISION OF BOSS PROJECTILE AND PLAYER
            if player.health >= 0:
                for ice in ices:
                    if ice.hitbox.colliderect(player.hitbox):
                        ice.jangle()
                        ice.kill()
                        player.health -= 1
                        print(f'PLAYER HP: {player.health}')
                        print("PLAYER was hit")
                        ices.remove(ice)
            
            # RESET HEALTH IF PLAYER HAS EXTRA LIFE
            if player.health == 0 and player.lives > 0:
                player.health = 12
                player.lives -= 1

            # PLAYER ANIMATION
            player.animate()

        # GET CURRENT TIME
        current_time = pygame.time.get_ticks()

        
        # RENDER DISPLAY
        pygame.display.flip()
        screen.blit(background, (0, 0)) # add background to screen

        # RENDER PLAYER IF IT IS ALIVE
        if player.health > 0:
            player_group.draw(screen) # create all sprites from specific group
        else:
            return GameEvent.GAMEOVER
        
        # RENDER BOSS IF IT IS ALIVE
        if boss.health > 0:
            boss_group.draw(screen)
        else:
            return GameEvent.GAMEOVER
        
        # RENDER PROJECTILES IF BOSS AND PLAYER ARE BOTH ALIVE
        if boss.health > 0 and player.health > 0 and ready:
            ice_group.draw(screen)
            bullet_group.draw(screen)
        
        # DRAW HP BARS
        healthbar_group.draw(screen)
        bosshealthbar_group.draw(screen)
        

        # UPDATE SPRITES
        player_group.update(PLAYER_X, PLAYER_Y, 0.25) # update the position of the all sprites in specific group
        bullet_group.update()
        boss_group.update(current_time, 0.25)
        ice_group.update()
        healthbar_group.update(player.health)
        bosshealthbar_group.update(boss.health)

        # HIT BOXES
        #if player.health > 0 and ready:
        #    player.draw(screen)
        #if boss.health > 0 and ready:
        #    boss.draw(screen)
        #if player.health > 0 and ready:
        #    for bullet in bullets:
        #        bullet.draw(screen)
        #if boss.health > 0 and ready:
        #    for ice in ices:
         #       ice.draw(screen)
        

        clock.tick(120)


def game_over(screen):
        
    game_over = Button(
        center_pos = (400, 400),
        font_size = 50,
        bg_color = BLACK,
        text_color = RED,
        text_content = 'GAME OVER',
        action = GameEvent.STATIC,
    )

    return_button = Button(
        center_pos = (400, 500),
        font_size = 30,
        bg_color = BLACK,
        text_color = RED,
        text_content = 'start over?',
        action = GameEvent.STARTOVER,
    )

    buttons = RenderUpdates(return_button, game_over)

    pygame.mouse.set_visible(True)

    running = True
    while running:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            
            button.draw(screen)
        pygame.display.flip()
        screen.blit("assets/frost.png", (0, 0)) # add background to screen
import pygame, sys, random
from pygame.locals import *
from classes.player import Player
from classes.apple import Apple
from classes.button import Button
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, PLAYER_IMAGE
from utils import START_BUTTON_IMG, ROTTEN_APPLE_IMAGE, APPLE_IMAGE, GOLD_APPLE_IMAGE


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Apple Fall')
    fps = pygame.time.Clock()
    global myfont
    myfont = pygame.font.SysFont("monospace", 26)
    global score
    score = 0
    global missed_apples
    missed_apples = 0
    #PLAYER
    player_sprites = pygame.sprite.Group()
    global player
    player = Player(pos_x=SCREEN_WIDTH/2, pos_y=600, speed=10, image=PLAYER_IMAGE)
    player_sprites.add(player)

    #GOOD APPLE
    good_apple_sprites = pygame.sprite.Group()

    good_apple = Apple(image=APPLE_IMAGE, speed=5)
    good_apple_sprites.add(good_apple)

    #ROTTEN APPLE
    rotten_apple_sprites = pygame.sprite.Group()

    rotten_apple = Apple(image=ROTTEN_APPLE_IMAGE, delay=-100)
    rotten_apple2 = Apple(image=ROTTEN_APPLE_IMAGE, delay=-100)
    rotten_apple_sprites.add(rotten_apple, rotten_apple2)

    #GOLD APPLE
    gold_apple_sprites = pygame.sprite.Group()
    gold_apple = Apple(image=GOLD_APPLE_IMAGE)
    gold_apple_sprites.add(gold_apple)
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
     

        #COLLISION SECTION
        sprite_hit = pygame.sprite.spritecollide(player, good_apple_sprites, False)

        for hit in sprite_hit:
            good_apple.rect.center = random.randint(0, SCREEN_WIDTH), 0
            score += 1
        
        rotten_apple_hit = pygame.sprite.spritecollide(player, rotten_apple_sprites, False)

        for hit in rotten_apple_hit:
            rotten_apple.rect.center = random.randint(0, SCREEN_WIDTH), 0
            player.life -= 1

        gold_apple_hit = pygame.sprite.spritecollide(player, gold_apple_sprites, False)
        
        for _ in gold_apple_hit:
            player.life += 1
            gold_apple.kill()
            gold_apple.rect.center = -10, -10
            score += 1

        #SCREEN BLIT AND CONFIGURATIONS
        fps.tick(60)
        screen.fill((COLORS['WHITE']))
        screen.blit(BACKGROUND_IMAGE, (0,0))
        player.update(screen)
        
        if score >= 10:
            rotten_apple.update(screen)

        if score >= 30:
            rotten_apple2.update(screen)

        if score == 50:
            gold_apple.update(screen)
        if score == 100:
            gold_apple.update(screen)
        if score == 150:
            gold_apple.update(screen)
        if score == 200:
            gold_apple.update(screen)
        if score == 250:
            gold_apple.update(screen)
        if score == 300:
            gold_apple.update(screen)

        if player.life <= 0:
            game_over()

        good_apple.update(screen)

        if player.life >= 3:
            lifes_label = myfont.render(f'{player.life}', 1, (0, 255, 0))
            screen.blit(lifes_label, (5, 3))
        if player.life < 3:
            lifes_label = myfont.render(f'{player.life}', 1, (255, 0, 0))
            screen.blit(lifes_label, (5, 3))

        if good_apple.rect.top >= SCREEN_HEIGHT:
            good_apple.rect.top = 0
            good_apple.rect.center = (random.randint(0, SCREEN_WIDTH - 10), 0)
            missed_apples += 1

        if rotten_apple.rect.top >= SCREEN_HEIGHT:
            rotten_apple.rect.top = 0
            rotten_apple.rect.center = (random.randint(0, SCREEN_WIDTH - 10), 0)
            
        if rotten_apple2.rect.top >= SCREEN_HEIGHT:
            rotten_apple2.rect.top = 0
            rotten_apple2.rect.center = (random.randint(0, SCREEN_WIDTH - 10), 0)


        point_label = myfont.render(f'{score}', 1, (0,0,255))
        screen.blit(point_label, (SCREEN_WIDTH - 50, 0))
        pygame.display.flip()


def menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    #BUTTONS SECTION
    start_button = Button(image=START_BUTTON_IMG, pos_x=100, pos_y=100, scale=2)
    # exit_button = Button()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if start_button.action():
                main()
                break
        
        fps.tick(60)
        screen.fill(COLORS['WHITE'])
        start_button.update(screen)
        pygame.display.flip()


def game_over():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    while True:
        screen.fill(COLORS['RED'])
        gameover_label = myfont.render(f'GAME OVER! You have collected {score} apples and missed {missed_apples}.', 1, (255, 255, 0))
        play_again_label = myfont.render('Press ESC to play again.', 1, (255,255,0))
        screen.blit(play_again_label, (SCREEN_WIDTH / 2 - 200,  SCREEN_HEIGHT / 2 + 60))
        screen.blit(gameover_label, (SCREEN_WIDTH / 2 - 420, SCREEN_HEIGHT / 2))

        fps.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
        
        pygame.display.flip()

if __name__ == '__main__':
    menu()
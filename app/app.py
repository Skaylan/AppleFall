import pygame, sys, random
from pygame.locals import *
from classes.player import Player
from classes.apple import Apple
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, PLAYER_IMAGE, ROTTENAPPLE_IMAGE, APPLE_IMAGE


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Apple Fall')
    fps = pygame.time.Clock()
    global myfont
    myfont = pygame.font.SysFont("monospace", 26)
    global score
    score = 0
    life = 5

    #PLAYER
    player_sprites = pygame.sprite.Group()
    global player
    player = Player('Lucas', SCREEN_WIDTH/2, 600, 10, PLAYER_IMAGE)
    player_sprites.add(player)

    #GOOD APPLE
    good_apple_sprites = pygame.sprite.Group()
    global good_apple
    good_apple = Apple(image=APPLE_IMAGE)
    good_apple_sprites.add(good_apple)

    #ROTTEN APPLE
    rotten_apple_sprites = pygame.sprite.Group()
    global rotten_apple
    rotten_apple = Apple(image=ROTTENAPPLE_IMAGE, delay=-100)
    rotten_apple_sprites.add(rotten_apple)

    

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
            life -= 1
        #SCREEN BLIT AND CONFIGURATIOND
        fps.tick(60)
        screen.fill((COLORS['WHITE']))
        screen.blit(BACKGROUND_IMAGE, (0,0))
        player.update(screen)
        
        if score >= 10:
            rotten_apple.update(screen)

        if life <= 0:
            game_over()
        good_apple.update(screen)

        if life >= 3:
            lifes_label = myfont.render(f'{life}', 1, (0, 255, 0))
            screen.blit(lifes_label, (5, 3))
        if life < 3:
            lifes_label = myfont.render(f'{life}', 1, (255, 0, 0))
            screen.blit(lifes_label, (5, 3))

        point_label = myfont.render(f'{score}', 1, (0,0,255))
        screen.blit(point_label, (SCREEN_WIDTH - 50, 0))
        pygame.display.flip()

def game_over():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    while True:
        screen.fill(COLORS['RED'])
        gameover_label = myfont.render(f'GAME OVER! You have collected {score} apples.', 1, (255, 255, 0))
        play_again_label = myfont.render('Press ESC to play again.', 1, (255,255,0))
        screen.blit(play_again_label, (SCREEN_WIDTH / 2 - 200,  SCREEN_HEIGHT / 2 + 60))
        screen.blit(gameover_label, (SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2))

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
    main()
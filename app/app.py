import pygame, sys
from pygame.locals import *
from classes.player import Player
from classes.apple import Apple
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, PLAYER_IMAGE


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Apple Fall')
    FPS = pygame.time.Clock()
    player = Player('Lucas', SCREEN_WIDTH/2, 600, 10, PLAYER_IMAGE)
    good_apple = Apple()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
     


        FPS.tick(60)
        screen.fill((COLORS['WHITE']))
        screen.blit(BACKGROUND_IMAGE, (0,0))
        player.update(screen)
        good_apple.update(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
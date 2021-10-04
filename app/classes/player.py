import pygame
from pygame.locals import *
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, nome: str, pos_x: int, pos_y: int, speed: int, image: str):
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.nome = nome
        self.speed = speed
        self.flip = False

    def update(self, screen):
        '''
        :param class screen: pygame.Surface variable defined at the main function with pygame.display.set_mode().
        '''
        screen.blit(self.image, self.rect)

        #PLAYER MOVEMENTS
        #CHECK FOR KEYS EVENT
        keys = pygame.key.get_pressed()
        if self.flip == True:
            self.image = pygame.transform.flip(self.image, True, False)
        

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.flip(self.image, True, False)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = pygame.image.load(self.image_path)
            self.flip = True
            self.flip = False

        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_DOWN]:
        #     self.rect.y += self.speed

        #AVOID PLAYER GET OFF SCREEN
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    

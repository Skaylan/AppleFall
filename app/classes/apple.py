import pygame, random
from pygame.locals import *
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT



class Apple(pygame.sprite.Sprite):
    def __init__(self, image: str = None, speed: int = 7, delay: int =0):
        '''
        :param image str: the path to a image:
        :param speed int: the speed in pixels that the object will move:
        :param delay int: must be a negative integer to delay the object:
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (20*2, 20*2))
        self.rect.center = (random.randint(0, SCREEN_WIDTH - 10), 0)
        self.speed = speed

    def update(self, screen):
        '''
        :param class screen: pygame.Surface variable defined at the main function with pygame.display.set_mode().
        '''
        screen.blit(self.image, self.rect)

        #APPLE MOVEMENT
        self.rect.y += self.speed

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(0, SCREEN_WIDTH - 10), 0)
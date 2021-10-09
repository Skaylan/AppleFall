import pygame
from pygame.locals import *
from utils import COLORS, SCREEN_WIDTH, SCREEN_HEIGHT


class Button():
    def __init__(self, image: str, pos_x: int, pos_y: int, scale: int = 0):
        self.scale = scale
        self.image = pygame.image.load(image).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*self.scale), int(height*self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.clicked = False

    def update(self, screen):
        screen.blit(self.image, self.rect)
    
    def action(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        #CHECK MOUSE HOVER AND EVENTS
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        return action
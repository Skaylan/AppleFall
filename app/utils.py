import pygame
from pygame.locals import *
COLORS = {'BLACK': (0,0,0), 'WHITE': (255,255,255), 'RED': (255,0,0)}
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 508
PLAYER_IMAGE = 'assets/images/isaacnewton.png'
ROTTEN_APPLE_IMAGE = 'assets/images/rottenapple.png'
APPLE_IMAGE = 'assets/images/apple.png'
GOLD_APPLE_IMAGE = 'assets/images/goldapple.png'
BACKGROUND_IMAGE = pygame.image.load('assets/images/doubletree.png')
missed_apples = 0
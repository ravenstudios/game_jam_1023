from constants import *
import pygame


class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, width=BLOCK_SIZE, height=BLOCK_SIZE):
        super().__init__()
        self.width = width
        self.height = height



        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
    
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)









    def update(self):
        self.rect.top += 1

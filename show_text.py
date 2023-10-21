from constants import *
import pygame



class Show_text():
    def __init__(self, text, size, x, y, surface):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = self.font.render(text, True, GREEN, BLUE)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x // 2, y // 2)
        surface.blit(self.text, self.textRect)

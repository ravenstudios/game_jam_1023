from constants import *
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


        # self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        # self.y_sprite_sheet_index = y_sprite_sheet_index

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((255, 255, 0))
        # self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect())

        self.rect.bottomleft = ((GAME_WIDTH // 2) - (BLOCK_SIZE // 2), GAME_HEIGHT)

        self.speed = 5



    def update(self, objects):

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GAME_WIDTH:
            self.rect.right = GAME_WIDTH
        self.keys()
        self.collide(objects)


    def collide(self, objects):
        print(pygame.sprite.spritecollide(self, objects, True))

    def keys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.left += self.speed

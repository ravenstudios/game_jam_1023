import pygame
import random
import object
from constants import *


pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

player_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()

number_candy = random.randint(0, 100)
for _ in range(number_candy):
    random_x = random.randint(0, GAME_WIDTH)
    obj = object.Object(random_x, 0)
    object_group.add(obj)
for o in object_group:


pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()
        draw()

    pygame.quit()


def draw():
    surface.fill((0, 0, 10))#background
    player_group.draw(surface)
    object_group.draw(surface)
    pygame.display.flip()


def update():
    player_group.update()
    object_group.update()


if __name__ == "__main__":
    main()

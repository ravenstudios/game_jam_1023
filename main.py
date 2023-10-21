import pygame
import random


pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

player_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()

number_candy = random.randint(3, 10)
for _ in range(number_candy):
    random_x = random.randint(0, GAME_WIDTH)
    obj = Object(random_x, 0)
    object_group.add(obj)


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
    surface.fill((10, 30, 123))  # background
    player_group.draw(surface)
    object_group.draw(surface)
    pygame.display.flip()


def update():
    player_group.update()
    object_group.update()


if __name__ == "__main__":
    main()

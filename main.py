from constants import *
import pygame
import object


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

obj = object.Object(20, 20)
player_group = pygame.sprite.Group()
player_group.add(obj)

pygame.init()



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 10))#background

    player_group.draw(surface)


    pygame.display.flip()


def update():
    player_group.update()



if __name__ == "__main__":
    main()

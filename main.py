from constants import *
import pygame
import state_manager


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))




pygame.init()

sm = state_manager.State_manager()

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
    sm.draw(surface)
    pygame.display.flip()


def update():
    sm.update()



if __name__ == "__main__":
    main()

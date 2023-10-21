from constants import *
import pygame
import state_manager


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))



sm = state_manager.State_manager()
pygame.init()



def main():

    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                sm.set_event_key(event.key)

            # sm.set_event_key(event.key)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                # sm.set_event_key(event.key)
                if event.key == pygame.K_q:
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

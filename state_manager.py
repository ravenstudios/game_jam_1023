import object
import pygame

class State_manager:
    def __init__(self):
        self.state = None
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(object.Object(20, 20))
        pass



    def draw(self, surface):
        self.game_objects.draw(surface)

    def update(self):
        self.game_objects.update()


    def get_state(self):
        return self.state

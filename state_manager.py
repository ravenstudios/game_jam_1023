import object
import pygame
import show_text
import player



class State_manager:
    def __init__(self):
        self.state = None
        self.game_objects = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.game_objects.add(object.Object(20, 20))
        self.player_group.add(player.Player())
        self.states = [
            {"name":"main_screen",
                "draw": self.main_screen,
                "update": self.main_screen
             },

            {"name":"running",
                "draw": self.running,
                "update": self.running,
            },

            {"name":"pause",
                "draw": self.pause,
                "update": self.pause,
            },

            {"name":"end",
                "draw": self.end,
                "update": self.end,
            }
        ]

        self.event_key = None

        self.state = self.states[0]



    def main_screen(self, mode, surface=None):
        if mode == "draw":
            text = "Start screen. \\nPress any key to start!!!"
            size = 32
            x = 300
            y = 300
            st = show_text.Show_text(text, size, x, y, surface)
        if mode == "update":
            if self.event_key:
                self.state = self.states[1]



    def running(self, mode, surface=None):
        if mode == "draw":
            self.player_group.draw(surface)
            self.game_objects.draw(surface)
        if mode == "update":
            self.player_group.update(self.game_objects)
            self.game_objects.update()

            if self.event_key == pygame.K_p:
                self.event_key = None
                self.state = self.states[2]
                return




    def pause(self, mode, surface=None):

        if mode == "draw":
            text = "Pause screen"
            size = 32
            x = 300
            y = 300
            st = show_text.Show_text(text, size, x, y, surface)
        if mode == "update":
            if self.event_key == pygame.K_p:
                self.event_key = None
                self.state = self.states[1]
                return



    def end(self, mode, surface=None):
        if mode == "draw":
            text = "End screen"
            size = 32
            x = 300
            y = 300
            st = show_text.Show_text(text, size, x, y, surface)

        if mode == "update":
            pass



    def draw(self, surface):
        self.state["draw"]("draw", surface)




    def update(self):
        self.state["update"]("update")

    def set_state(self, state):
        self.state = self.states[state]


    def get_state(self):
        return self.state

    def set_event_key(self, key):
        self.event_key = key

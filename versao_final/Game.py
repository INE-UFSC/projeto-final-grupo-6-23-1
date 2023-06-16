import pygame
from pygame.locals import *
import sys
from Match import Match


class Game:
    def __init__(self, config): 
        self.__config = config
        self.__width = 640
        self.__height = 360
        self.__screen = pygame.display.set_mode((self.__width, self.__height))  #essa informação deve vir de config
        self.__match = Match(self.__screen)
        pygame.display.set_caption('Goal Masters')
        self.__background = pygame.Surface(self.__screen.get_size())
        self.__running = False
        self.__fps: int = 60
        self.__timer = pygame.time.Clock()

    def start_game(self):
        pygame.init()
        self.__running = True
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.loop()

    def loop(self):
        while self.__running:
            self.__timer.tick(self.__fps)
            events = self.handle_events()
            self.process_input(events)
            self.update_time(events)
            self.draw_frame()
            self.render()

        self.quit()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.__running = False

        return events

    def process_input(self, events):
        self.__match.process_input(events, self.__screen)

    def update_time(self, events):
        self.__match.update_time(events)

    def draw_frame(self):
        self.__match.draw(pygame, self.__screen)

    def render(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def show_menu(self):
        pass

import pygame
from pygame.locals import *
import sys
from Match import Match
from GameConfig import GameConfig


class Game:
    def __init__(self, config: GameConfig): 
        self.__config = config
        #Example on how to change the map
        #self.__config.set_map('desert')
        self.__width = self.__config.get_screen_width()
        self.__height = self.__config.get_screen_height()
        self.__screen = pygame.display.set_mode((self.__width, self.__height))  #essa informação deve vir de config
        self.__match = None
        pygame.display.set_caption('Goal Masters')
        self.__background = pygame.Surface(self.__screen.get_size())
        self.__running = False
        self.__fps: int = self.__config.get_fps()
        self.__timer = pygame.time.Clock()

    def start_game(self):
        pygame.init()
        self.__match = Match(self.__screen, self.__config.get_map())
        self.__running = True
        self.loop()

    def loop(self):
        while self.__running:
            self.__timer.tick(self.__fps)
            events = self.handle_events()
            self.process_input(events)
            self.__match.handle_events(events,self.__screen)
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

    def draw_frame(self):
        self.__match.draw(pygame, self.__screen)

    def render(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def show_menu(self):
        pass

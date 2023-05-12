import pygame
from pygame.locals import *
import sys
from Match import Match

class Game:
    def __init__(self, config): 
        self.__config = config
        self.__match = Match()
        self.__screen = pygame.display.set_mode((150, 50))  #essa informação deve vir de config
        self.__background = pygame.Surface(self.__screen.get_size())
        self.__running = False
        self.__fps: int = 60

    def start_game(self):
        pygame.init()
        self.__running = True
        fps = pygame.time.Clock()
        fps.tick(self.__fps)
        self.loop()

    def loop(self):
        while self.__running:
            events = self.handle_events()
            self.process_input(events)
            self.draw_frame()
            self.render()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event == QUIT:
                self.quit()

        return events
    
    def process_input(self, events):
        self.__match.process_input(events)

    def draw_frame(self):
        self.__match.draw(pygame, self.__screen)

    def render(self):
        pygame.display.flip()

    def quit(self):
        self.__running = False
        pygame.quit()
        sys.exit()

    def show_menu(self):
        pass
    
    def end_game(self):
        pass
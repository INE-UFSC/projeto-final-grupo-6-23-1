import pygame
from pygame.locals import *
from GameObject import GameObject

class Match:
    def __init__(self):
        self.__game_objects: list[GameObject] = []
        self.__cenario = None
        self.__time: int = 0

    def check_collisions(self):
        for game_obj in self.__game_objects:
            game_obj.check_collisions(self.__game_objects)

    def draw_score(self):
        pass
    
    def process_input(self, events):
        pass

    def draw(self):
        for obj in self.__game_objects:
            obj.draw()

        self.draw_score()

    def check_goal(self):
        #can be implemented with custom event, ex
        """
        suppose that the event is called GOAL, and it's implemented as such:
            GOAL = pygame.USEREVENT + 1

            it can be send to the events list in pygame using:
            ev = pygame.event.Event(GOAL)
            pygame.event.post(ev)

            then check_goal() can receive events and then handle the pygame event GOAL
        """
        pass

    def update_time():
        pass


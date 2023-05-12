import pygame
from pygame.locals import *
from GameObject import GameObject
from Player import Player
from MovingObjects import MovingObjects

class Match:
    def __init__(self):
        self.__game_objects: list[GameObject] = [
            Player(20, 20, 0, 0, 5, 5, 0),
            Player(20, 20, 40, 0, 5, 5, 1)
        ]
        self.__cenario = None
        self.__time: int = 0

    def check_collisions(self):
        for game_obj in self.__game_objects:
            game_obj.check_collisions(self.__game_objects)

    def draw_score(self):
        pass
    
    def process_input(self, events):
        for obj in self.__game_objects:
            if isinstance(obj, MovingObjects):
                obj.move(events)

    def draw(self, pg: pygame, surface: pygame.Surface):
        surface.fill((0, 0, 0)) #it clears the previous frame to draw a new one
                                #to do - implement cenario

        for obj in self.__game_objects:
            obj.draw(pg, surface)

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


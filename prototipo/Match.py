import pygame
from pygame.locals import *
from GameObject import GameObject
from Player import Player
from Ball import Ball
from MovingObjects import MovingObjects


class Match:
    def __init__(self):
        self.__game_objects: list[GameObject] = [
            Player(20, 20, 0, 0, 5, 5, 0),
            Player(20, 20, 80, 0, 5, 5, 1),
            Ball(20, 20, 40, 0, 20, 0, 20)
        ]
        self.__cenario:str = 'test'
        self.__time: int = 0
        self.__gravity = 0.7

    """ def check_collisions(self):
        for game_obj in self.__game_objects:
            game_obj.check_collisions(self.__game_objects) """

    def draw_time(self):
        self.update_time()
        font = pygame.font.Font(None, 40)
        text = font.render(str(self.__time), False, 'White')
        return text

    def draw_score(self):
        scores = self.update_score()
        font = pygame.font.Font(None, 40)
        text_player1 = font.render(str(scores[0]), False, 'White')
        text_player2 = font.render(str(scores[1]), False, 'White')
        return [text_player1, text_player2]

    def process_input(self, events, screen):
        for obj in self.__game_objects:
            if isinstance(obj, MovingObjects):
                obj.move(
                    events= events, 
                    screen= screen, 
                    game_objects= self.__game_objects, 
                    gravity= self.__gravity
                )

    def draw(self, pg: pygame, surface: pygame.Surface):
        surface.fill((0, 0, 0)) #it clears the previous frame to draw a new one
        if self.__cenario == 'test': #to do - implement cenario
            background = pygame.image.load('sprites/stages/test/background.png')
            ground = pygame.image.load('sprites/stages/test/ground.png')
        surface.blit(background, (0,0))
        surface.blit(ground, (0,288))

        for obj in self.__game_objects:
            obj.draw(pg, surface)

        surface.blit(self.draw_time(), (300,5))

        surface.blit(self.draw_score()[0], (0, 5))
        surface.blit(self.draw_score()[1], (0, 60))

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

    def update_time(self):
        pass

    def update_score(self):
        for obj in self.__game_objects:
            if isinstance(obj, Ball):
                if obj.get_pos_x() <= 30:
                    self.__game_objects[0].add_goals()
                    self.reset()
                elif obj.get_pos_x() >= 610:
                    self.__game_objects[1].add_goals()
                    self.reset()

        score_player1 = self.__game_objects[0].get_goals()
        score_player2 = self.__game_objects[1].get_goals()
        return [score_player1, score_player2]
    
    def reset(self):
        for obj in self.__game_objects:
            obj.set_pos(320,200)
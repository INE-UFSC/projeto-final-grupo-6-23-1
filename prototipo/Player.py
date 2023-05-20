from Character import Character
from pygame import Rect, event
import pygame
from pygame.locals import *
from utils import BUFF_APPLIED, DEBUFF_APPLIED

class Player(Character):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, controller: int):
        goals = 0
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, goals)
        self.__controller = controller
        # maybe create an object?
        self.__controllers = [
            {
                "UP": pygame.K_UP,
                "DOWN":  pygame.K_DOWN,
                "LEFT": pygame.K_LEFT,
                "RIGHT": pygame.K_RIGHT
            },
            {
                "UP": pygame.K_w,
                "DOWN":  pygame.K_s,
                "LEFT": pygame.K_a,
                "RIGHT": pygame.K_d
            },
        ]

    def move(self, events: event, **args):
        controller = self.__controllers[self.__controller]

        pos_x = self.get_pos_x()
        pos_y = self.get_pos_y()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        for event in events:
            if event.type == KEYDOWN:
                if event.key == controller["UP"]:
                    if pos_y > 0:
                        pos_y = pos_y - speed_y
                if event.key == controller["LEFT"]:
                    if pos_x > 0:
                        pos_x = pos_x - speed_x
                if event.key == controller["RIGHT"]:
                    if pos_x < 620:
                        pos_x = pos_x + speed_x

        if pos_y < 268:
            pos_y = pos_y + speed_y
        else:
            pos_y = 268

        new_rect = Rect(pos_x, pos_y, self.get_rect().width, self.get_rect().height)
        self.set_rect(new_rect)

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 0, 0), self.get_rect())

    def handle_events(self, events: event):
        for event in events:
            if event.type == BUFF_APPLIED:
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height) * 1.5)
                self.set_rect(new_rect_applied)
        
            elif event.type == DEBUFF_APPLIED:
                player_min = self.get_rect().height * 0.5
                new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height + player_min)
                self.set_rect(new_rect_debuff)
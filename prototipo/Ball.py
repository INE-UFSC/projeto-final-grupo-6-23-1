from MovingObjects import MovingObjects
import pygame
from pygame import Rect, event
from pygame.locals import *

class Ball(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y)

    def move(self, events: event):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 255, 255), self.get_rect())

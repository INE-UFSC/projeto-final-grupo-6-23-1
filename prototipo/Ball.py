from MovingObjects import MovingObjects
import pygame
from pygame import Rect, event
from pygame.locals import *

class Ball(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, radius: int):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y)
        self.__radius = radius

    def check_gravity(self, width, height):
        speed_y = self.get_speed_y()
        speed_x = self.get_speed_x()

        if self.get_pos_y() < height - self.radius:
            self.set_speed_y(speed_y + 0.5)
        else:
            if speed_y > 0.3:
                self.set_speed_y(speed_y * -1 * 0.9) #0.9 is retention
            else:
                if abs(speed_y) <= 0.3:
                    self.set_speed_y(0)

    def move(self, events: event, screen: pygame.display):
        self.check_gravity(screen.get_width, screen.get_height)

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 255, 255), self.get_rect())

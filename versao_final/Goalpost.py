from GameObject import GameObject
from pygame import event, Rect
from pygame.locals import *
import pygame


class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)
    
    def handle_events(self,events: event):
        pass
    
    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (0, 0, 255), self.get_rect())

from GameObject import GameObject
from Ball import Ball
from pygame import event, Rect
from pygame.locals import *
import pygame
from Player import Player

class Ground(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)

    def handle_events(self, events: event):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (0, 255, 0), self.get_rect())

    def check_collision(self, width: int, height: int, player: Player, objects: list[GameObject]):
        pass
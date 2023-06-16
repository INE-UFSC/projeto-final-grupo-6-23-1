from GameObject import GameObject
from pygame import event, Rect
from pygame.locals import *
import pygame

class Ground(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, sprite):
        super().__init__(width, height, pos_x, pos_y)
        self.__sprite = sprite

    def handle_events(self, events: event):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

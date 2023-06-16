from GameObject import GameObject
from pygame import event, Rect
from pygame.locals import *
import pygame
from utils import BUFF_APPLIED, DEBUFF_APPLIED
class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)
    
    def handle_events(self,events: event):
        """for event in events:
            if event.type == BUFF_APPLIED:
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y, self.get_rect().width,(self.get_rect().height) * 1.5)
                self.set_rect(new_rect_applied)
        
            elif event.type == DEBUFF_APPLIED:
                goalpost_min = self.get_rect().height * 0.5
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - goalpost_min)
                self.set_rect(new_rect_applied)"""
        pass
    
    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (0, 0, 255), self.get_rect())

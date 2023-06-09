from GameObject import GameObject
from Ball import Ball
from pygame import event, Rect
from pygame.locals import *
import pygame
from utils import BUFF_APPLIED, DEBUFF_APPLIED
from Player import Player
class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)

    def check_goal(self, ball: Ball):
        if Rect.colliderect(self.get_rect(), ball.get_rect()): #to do #new logic with line, when the ball collides with the line, then return True
            return True
        else:
            return False
    
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
    
    def check_collision(self,width: int, height: int, player: Player, objects: list[GameObject]):
        for obj in objects:
            if isinstance(object,player):
                player.collision_with_screen(obj)
        player.collision_with_screen(width, height)

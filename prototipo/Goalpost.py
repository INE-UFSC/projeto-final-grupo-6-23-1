from GameObject import GameObject
from Ball import Ball
from pygame import event
import pygame
from utils import BUFF_APPLIED, DEBUFF_APPLIED

class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)
        pygame.time.set_timer(BUFF_APPLIED, 100) #set event timer

    def check_goal(self, ball: Ball) -> bool:
        if self.get_rect().colliderect(ball.get_rect()): #to do #new logic with line, when the ball collides with the line, then return True
            return True
        else:
            return False
    
    def handle_events(self,events: event):
        for event in events:
            if event.type == BUFF_APPLIED:
                self.set_height(self.get_height() * 1.5)
        
            elif event.type == DEBUFF_APPLIED:
                self.set_height(self.get_height() - (self.get_height() * 0.5))
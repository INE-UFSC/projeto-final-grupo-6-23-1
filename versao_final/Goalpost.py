from GameObject import GameObject
from pygame import event, Rect
from pygame.locals import *
import pygame
from utils import BUFF_APPLIED, DEBUFF_APPLIED, get_file_path
class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, side: str):
        super().__init__(width, height, pos_x, pos_y)
        
        # Load image
        image_path = get_file_path('sprites', 'goalpost.png')
        self.__sprite = pygame.image.load(image_path)

        # Inverts image horizontally if not player one (player in the left)
        if side == 'right':
            self.__sprite = pygame.transform.flip(self.__sprite, True, False)
    
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
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

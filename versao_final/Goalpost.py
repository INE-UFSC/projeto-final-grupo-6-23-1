from GameObject import GameObject
from pygame import event, Rect
from pygame.locals import *
import pygame
from utils import *
class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, side: str):
        super().__init__(width, height, pos_x, pos_y)
        
        # Load image
        image_path = get_file_path('sprites', 'goalpost.png')
        self.__sprite = pygame.image.load(image_path)
        self.__side = side
        # Inverts image horizontally if not player one (player in the left)
        if self.__side == 'right':
            self.__sprite = pygame.transform.flip(self.__sprite, True, False)
    
    def handle_events(self,events: event):
        for event in events:
            if event.type == BUFF_APPLIED  and event.collectable_type == 'size_down_goalpost' :
                if event.target == "right_goalpost" and self.get_side() == 'right':
                    player_min = self.get_rect().height * 0.5
                    new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min )
                    self.set_rect(new_rect_debuff)
                elif event.target == "left_goalpost" and self.get_side() == 'left':
                    player_min = self.get_rect().height * 0.5
                    new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min )
                    self.set_rect(new_rect_debuff)
        
            elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'size_up_goalpost' and self == event.target:
                height = event.target.get_rect().height
                self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height * 2))
                self.set_rect(new_rect_applied)

            #elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'fronzen' and self == event.target:

            if event.type == RESET_STATE and self == event.target:
                if event.collectable_type == 'size_down_player':
                   event.target.get_rect().height *= 0.5 
                
                elif event.collectable_type == 'size_up_player':
                    height = event.target.get_rect().height
                    self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                    event.target.get_rect().height *=2
                    
    
    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

    def get_side(self):
        return self.__side

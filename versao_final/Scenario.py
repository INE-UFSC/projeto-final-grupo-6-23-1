import pygame
from pygame import Rect
from utils import get_file_path
from Ground import Ground

#valid types = 'default', 'desert'
class Scenario:
    def __init__(self, surface, type_ = 'default'):
        self.__ground_image = None
        self.__background_sprite = None
        
        if type_ == 'default':
            self.__ground_image = pygame.image.load(get_file_path('sprites','stages','test','ground.png'))
            self.__background_sprite = pygame.image.load(get_file_path('sprites','stages','stadium.png'))
        elif type_ == 'desert':
            self.__ground_image = pygame.image.load(get_file_path('sprites','stages','desert_ground.png'))
            self.__background_sprite = pygame.image.load(get_file_path('sprites','stages','desert.jpg'))
        self.__ground = Ground(640, 72, 0, 288, self.__ground_image)
        self.__background = Rect(0, 0, surface.get_width(), surface.get_height() - self.__ground.get_height())
    
    def get_ground_height(self):
        return self.__ground.get_rect().height
    
    def get_structures(self):
        return [self.__ground]
    
    def draw_background(self, surface):
        rect = self.__background
        resized_sprite = pygame.transform.scale(self.__background_sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)
    


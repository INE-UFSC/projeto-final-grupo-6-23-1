import pygame
from pygame import Rect
from utils import get_image_path
from Ground import Ground

class Scenario:
    def __init__(self):
        self.__ground_image = pygame.image.load(get_image_path('sprites','stages','test','ground.png'))
        self.__ground = Ground(640, 72, 0, 288, self.__ground_image)
    
    def get_ground_height(self):
        return self.__ground.get_rect().height
    
    def get_structures(self):
        return [self.__ground]
    


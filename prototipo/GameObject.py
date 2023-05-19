from pygame import Rect
import pygame


class GameObject:
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        self.__rect = Rect(pos_x, pos_y, width, height)

    # getters
    def get_width(self) -> int:
        return self.__rect.width
    
    def get_height(self) -> int:
        return self.__rect.height
    
    def get_pos_x(self) -> int:
        return self.__rect.x
    
    def get_pos_y(self) -> int:
        return self.__rect.y
    
    def set_pos(self, pos_x: int, pos_y: int):
        self.__rect.x = pos_x
        self.__rect.y = pos_y

    def get_rect(self) -> Rect:
        return self.__rect
    
    def set_rect(self, rect: Rect):
        self.__rect = rect
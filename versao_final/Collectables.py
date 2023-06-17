from abc import ABC, abstractmethod
from GameObject import GameObject
import pygame
import random
from pygame import Rect
class Collectables(GameObject, ABC):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)
        self.duration = duration
        self.type = type

    @abstractmethod
    def check_collision(self, objects: list[GameObject]):
        pass

    def disappear(self, objects: list[GameObject]):
        objects_without_collectables = [obj for obj in objects if not isinstance(obj, Collectables)]
        objects.clear()
        objects.extend(objects_without_collectables)

    #Get the duration of the collectable.  
    def get_duration(self) -> float:
        return self.duration

    #Set the duration of the collectable.
    def set_duration(self, duration: float) -> None:
        self.duration = duration

    #Set the type of the collectable.   
    def set_type(self, type: str) -> None:
        self.type = type

    #Get the type of the collectable.
    def get_type(self) -> str:
        return self.type

    def set_to_random_position(self, objects: list[GameObject], screen: pygame.surface.Surface):
        height = screen.get_height()
        widht = screen.get_width()
        pos_x = random.randint(0,widht)
        pos_y = random.randint(0,height)
        new_rect = Rect(pos_x,pos_y,self.get_width(),self.get_height())
        is_collinding = False

        for obj in objects:
            if Rect.colliderect(new_rect, obj.get_rect()):
                is_collinding = True
        
        if not is_collinding:
            self.set_pos(pos_x, pos_y)
        
        else:
            self.set_to_random_position(objects, screen)
        

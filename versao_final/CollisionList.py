from pygame import Rect
from GameObject import GameObject
from MovingObjects import MovingObjects
from utils import get_obj_of_type

class CollisionList:
    def __init__(self, main_obj: MovingObjects, objects: list[GameObject]):
        self.__collisions: list = []
        self.__main_obj = main_obj
        self.__objects = objects

        self.__check_collisions()
        
    def __check_collisions(self):
        objects = []
        for obj in self.__objects:
            if obj != self.__main_obj:
                objects.append(obj)

        rects = [obj.get_rect() for obj in objects]
        collide_indexes = Rect.collidelistall(self.__main_obj.get_rect(), rects)
        
        self.__collisions = list(map(objects.__getitem__, collide_indexes))

    def get_collisions(self):
        return self.__collisions
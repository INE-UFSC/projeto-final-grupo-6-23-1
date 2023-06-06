from abc import ABC, abstractmethod
from GameObject import GameObject

class MovingObjects(GameObject, ABC):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass: float):
        super().__init__(width, height, pos_x, pos_y)
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__mass = mass

    @abstractmethod
    def move(self):
        pass
    
    def check_collisions(self):
        pass #to do - implement collision behaviours

    def get_speed_x(self) -> float:
        return self.__speed_x
    
    def get_speed_y(self) -> float:
        return self.__speed_y
    
    def get_mass(self) -> float:
        return self.__mass
    
    def set_speed_x(self, speed_x: float):
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y: float):
        self.__speed_y =  speed_y

    def set_mass(self, mass: float):
        self.__mass = mass
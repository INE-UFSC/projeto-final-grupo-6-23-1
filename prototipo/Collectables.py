from abc import ABC, abstractmethod
from GameObject import GameObject
class Collectables(GameObject,ABC):
    def _init_(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super()._init_(width, height, pos_x, pos_y)
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

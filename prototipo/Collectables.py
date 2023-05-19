import pygame
from abc import ABC, abstractmethod
from GameObject import GameObject
from Ball import Ball
from Goalpost import Goalpost
from pygame import Rect
class Collectables(GameObject,ABC):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)
        self.duration = duration
        self.type = type

    #Check if the player or ball collide with the collectable. 
    def check_collision(self, objects: list[GameObject]):
        for obj in objects:
            if isinstance(obj, Ball) and Rect.colliderect(obj.get_rect(), self.get_rect()):
                """for game_obj in objects:
                    if isinstance(game_obj, Goalpost) and game_obj.get_player() != obj.get_last_touched_player(): 
                        current_height = game_obj.get_height()
                        new_height = current_height * 1.5
                        game_obj.set_height(new_height)
                        break
                break"""
    
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

    """
    @abstractmethod
    def update(self) -> None:
        Update the collectable sprite
        pass"""

     #Activate the collectable effect.
    """
    @abstractmethod
    def activate(self) -> None:
        pass"""
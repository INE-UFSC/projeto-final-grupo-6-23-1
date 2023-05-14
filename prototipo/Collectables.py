import pygame
from abc import ABC, abstractmethod
from GameObject import GameObject
class Collectables(GameObject,ABC,pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)
        self.duration = duration
        self.type = type

    #Check if the player or ball collide with the collectable. 
    def check_collision(self, player: pygame.sprite.Sprite, ball: pygame.sprite.Sprite) -> bool:
        return self.rect.colliderect(player.rect) or self.rect.colliderect(ball.rect)
    
    
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
import random
import pygame
from Collectables import Collectables

class Debuff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)

    #Generate a random debuff for the match
    def gen_random_debuff(self) -> None:
        self.duration = random.uniform(5.0, 20.0)  # Random duration between 5.0 and 20.0 seconds
        self.type = random.choice(['slow', 'reverse', 'confusion'])  # Random type of debuff
         #this is a test code, implement when have the ideias of buffs

    #Apply the debuff to a game object.
    def apply_debuff(self, game_object: pygame.sprite.Sprite) -> None:
        if self.type == 'slow':
            game_object.speed *= 0.5  # Decrease the game object's speed by 50%
        elif self.type == 'reverse':
            game_object.direction *= -1  # Reverse the game object's direction
        elif self.type == 'confusion':
            game_object.confused = True  # Confuse the game object
        #test code
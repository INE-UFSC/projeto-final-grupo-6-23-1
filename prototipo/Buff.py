import random
import pygame
from Collectables import Collectables

class Buff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)

    # Generate a random buff for the match.
    def gen_random_buff(self) -> None:
        self.duration = random.uniform(5.0, 20.0)  # Random duration between 5.0 and 20.0 seconds
        self.type = random.choice(['speed', 'invisibility', 'freeze'])  # Random type of buff
        #this is a test code, implement when have the ideias of buffs

    
    #Apply the buff to a game object
    def apply_buff(self, game_object: pygame.sprite.Sprite) -> None:
        if self.type == 'speed':
            game_object.speed *= 1.5  # Increase the game object's speed by 50%
        elif self.type == 'invisibility':
            game_object.visible = False  # Make the game object invisible
        elif self.type == 'freeze':
            game_object.frozen = True  # Freeze the game object
        #test code
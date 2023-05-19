import random
import pygame
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
class Buff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y,duration,self.gen_rand_buff())

    # Generate a random buff for the match.
    def gen_rand_buff(self) -> str:
        buffs = ['size_up']
        return random.choice(buffs)

    def apply_buff(self):
        if self.get_type == 'size_up':
            self.size_up(list[GameObject],Goalpost)

    def size_up(self,object: list[GameObject],obj_type):
        for obj in object:
            if isinstance(obj,obj_type):
                obj.set_height(obj.get_height()*1.5)
                
    

   # def apply_buff_to_goalpost(self, goalpost: Goalpost):
        """buff = self.gen_rand_buff()
        if buff == 'size_up':
            current_height = goalpost.get_height()
            new_height = current_height * 1.5
            goalpost.set_height(new_height)"""
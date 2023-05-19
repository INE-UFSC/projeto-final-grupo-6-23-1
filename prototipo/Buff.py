import random
from pygame import Rect
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
class Buff(Collectables):
    def _init_(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super()._init_(width, height, pos_x, pos_y,duration,self.gen_rand_buff())

    # Generate a random buff for the match.
    def check_collision(self, objects: list[GameObject]):
        collided = False
        for obj in objects:
            if Rect.colliderect(self.get_rect(), obj.get_rect()):
                if isinstance(obj, Ball):
                    self.apply_buff(obj)
                    collided = True

                elif isinstance(obj, Player):
                    self.apply_buff(obj)
                    collided = True

                elif isinstance(obj, Goalpost):
                    self.apply_buff(obj)
                    collided = True

                if collided:
                    self.disappear(objects)
                    return True

        return False
    
    def gen_rand_buff(self):
        buffs = ['size_up']
        return random.choice(buffs)

    def apply_buff(self):
        if self.get_type() == 'size_up':
            self.size_up(list[GameObject],Goalpost)

    def size_up(self,object: list[GameObject],obj_type):
        for obj in object:
            if isinstance(obj,obj_type):
                obj.set_height(obj.get_height()*1.5)
                
import random
import pygame
from pygame import Rect
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
from utils import DEBUFF_APPLIED

class Debuff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float):
        super().__init__(width, height, pos_x, pos_y,duration, self.gen_rand_debuff())

    
    def check_collision(self, objects: list[GameObject]):
        collided = False

        for obj in objects:
            if Rect.colliderect(self.get_rect(), obj.get_rect()):
                if isinstance(obj, Ball):
                    self.apply_debuff(obj)
                    collided = True

                elif isinstance(obj, Player):
                    self.apply_debuff(obj)
                    collided = True

                elif isinstance(obj, Goalpost):
                    self.apply_debuff(obj)
                    collided = True

                if collided:
                    self.disappear(objects)
                    return True

        return False
    
    #Generate a random debuff for the match
    def gen_rand_debuff(self) -> str:
        debuffs = ['size_down']
        return random.choice(debuffs)

    def apply_debuff(self, object):
        if self.get_type() == 'size_down':
            pygame.event.post(pygame.event.Event(DEBUFF_APPLIED, target = object))
    
    def handle_events(self,events):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        print("to aqui")
        pg.draw.rect(surface, (0, 255, 0), self.get_rect())

    """ def size_down(self,object: list[GameObject],obj_type):
        for obj in object:
            if isinstance(obj,obj_type):
                obj.set_height(obj.get_height() - (obj.get_height ()* 0.5))"""
        
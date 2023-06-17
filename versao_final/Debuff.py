import random
import pygame
from pygame import Rect
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
from utils import DEBUFF_APPLIED, RESET_STATE

class Debuff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y,duration, type)

    def check_collision(self, objects: list[GameObject]):
        collided = False

        for obj in objects:
            if Rect.colliderect(self.get_rect(), obj.get_rect()):
                if isinstance(obj, Ball):
                    self.apply_debuff(obj)
                    collided = True

                """ elif isinstance(obj, Player):
                    self.apply_debuff(obj)
                    collided = True

                elif isinstance(obj, Goalpost):
                    self.apply_debuff(obj)
                    collided = True """

                if collided:
                    self.disappear(objects)
                    return True

        return False
    #Generate a random debuff for the match
    @classmethod
    def gen_rand_debuff(self) -> str:
        debuffs = ['size_down_player','frozen']
        return random.choice(debuffs)

    def apply_debuff(self, obj: Ball):
        if self.get_type() == 'size_down_player':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="size_down_player"), 10000,1)
            pygame.event.post(pygame.event.Event(DEBUFF_APPLIED, target = player))
        elif self.get_type() == 'fronzen':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="fronzen"), 10000,1)
            pygame.event.post(pygame.event.Event(DEBUFF_APPLIED, target = player))
    
    def handle_events(self,events):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 0, 0), self.get_rect())

        
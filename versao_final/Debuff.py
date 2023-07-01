import random
import pygame
from pygame import Rect
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
from utils import *

class Debuff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float):
        self.__sprite = None
        self.__debuffs = {
                        'size_down_player': get_file_path('sprites', 'collectables', 'size_down_player.png'),
                        'size_up_goalpost': get_file_path('sprites', 'collectables', 'size_up_goalpost.png'),
                        'frozen_player': get_file_path('sprites', 'collectables', 'frozen_player.png')
                        
                        }
        super().__init__(width, height, pos_x, pos_y,duration, self.gen_rand_debuff())
        

    def check_collision(self, objects: list[GameObject]):
        collided = False

        for obj in objects:
            if Rect.colliderect(self.get_rect(), obj.get_rect()):
                if isinstance(obj, Ball):
                    self.apply_debuff(obj)
                    self.erase_collectables()
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
    def gen_rand_debuff(self) -> str:
        debuffs_types = list(self.__debuffs.keys())
        debuff_type = random.choice(debuffs_types)
        self.__sprite = pygame.image.load(self.__debuffs[debuff_type])
        return debuff_type

    def apply_debuff(self, obj: Ball):
        if self.get_type() == 'size_down_player':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="size_down_player"), 10000,1)
            pygame.event.post(pygame.event.Event(DEBUFF_APPLIED, target = player, collectable_type = "size_down_player"))
        elif self.get_type() == 'frozen_player':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="frozen_player"), 10000,1)
            pygame.event.post(pygame.event.Event(DEBUFF_APPLIED, target = player, collectable_type = "frozen_player"))
    
    def handle_events(self,events):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

        
import random
import pygame
from pygame import Rect,event
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
from utils import *

class Buff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float):
        self.__sprite = None
        self.__buffs = {
                        'size_up_player': get_file_path('sprites', 'collectables', 'size_up_player.png'),
                        'size_down_goalpost': get_file_path('sprites', 'collectables', 'size_down_goalpost.png')
                        }
        super().__init__(width, height, pos_x, pos_y, duration, self.gen_rand_buff())
        self.start_time = None
        self.target = None
        

    def check_collision(self, objects: list[GameObject]):
        collided = False
        for obj in objects:
            if Rect.colliderect(self.get_rect(), obj.get_rect()):
                if isinstance(obj, Ball):
                    self.apply_buff(obj)
                    self.erase_collectables()
                    collided = True
                """elif isinstance(obj, Player):
                    self.apply_buff(obj)
                    collided = True
                elif isinstance(obj, Goalpost):
                    self.apply_buff(obj)
                    collided = True """

                if collided:
                    self.disappear(objects)
                    return True

        return False
    
    def update(self):
        if self.start_time is not None:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time >= self.duration * 1000:  # Verifica se o tempo decorrido é maior ou igual à duração em milissegundos
                self.remove_buff()
                self.start_time = None
    
    def gen_rand_buff(self):
        buffs_types = list(self.__buffs.keys())
        buff_type = random.choice(buffs_types)
        self.__sprite = pygame.image.load(self.__buffs[buff_type])
        return buff_type

    def apply_buff(self, obj: Ball):
        if self.get_type() == 'size_up_player':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="size_up_player"), 10000,1)
            pygame.event.post(pygame.event.Event(BUFF_APPLIED, target= player, collectable_type = "size_up_player"))
        elif self.get_type() == 'size_down_goalpost':
            player = obj.get_last_touched()
            pygame.time.set_timer(pygame.event.Event(RESET_STATE, target = player, collectable_type="size_down_goalpost"), 10000,1)
            pygame.event.post(pygame.event.Event(BUFF_APPLIED, target= player, collectable_type = "size_down_goalpost"))

    
        
    def handle_events(self, events):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)
    

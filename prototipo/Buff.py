import random
import pygame
from pygame import Rect,event
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
from utils import BUFF_APPLIED

class Buff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float):
        super().__init__(width, height, pos_x, pos_y, duration, self.gen_rand_buff())
        self.start_time = None
        self.target = None

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
                    self.start_time = pygame.time.get_ticks()
                    return True

        return False
    
        """ def update(self):
        if self.start_time is not None:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time >= self.duration * 1000:  # Verifica se o tempo decorrido é maior ou igual à duração em milissegundos
                self.remove_buff()
                self.start_time = None"""
    
    def gen_rand_buff(self):
        buffs = ['size_up']
        return random.choice(buffs)

    def apply_buff(self, obj):
        if self.get_type() == 'size_up':
            pygame.event.post(pygame.event.Event(BUFF_APPLIED, target=obj))
    
    def remove_buff(self):
        if self.get_type() == 'size_up':
            pygame.event.post(pygame.event.Event(BUFF_APPLIED, target=None))
        
    def handle_events(self, events):
        pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (0, 255, 0), self.get_rect())
    
    def reset_object(self, obj: list[GameObject]):
        self.width = 20
        self.height = 20
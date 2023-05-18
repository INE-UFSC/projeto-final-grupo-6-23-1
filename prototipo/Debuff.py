import random
import pygame
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player

class Debuff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y)

    #Generate a random debuff for the match
    def gen_rand_debuff(self) -> str:
        debuffs = ['froze', 'size_down']
        return random.choice(debuffs)

    def apply_debuff(self, game_obj: GameObject):
        if isinstance(game_obj, Ball):
            self.apply_debuff_to_ball(game_obj)
        elif isinstance(game_obj, Player):
            self.apply_debuff_to_player(game_obj)
        elif isinstance(game_obj, Goalpost):
            self.apply_debuff_to_goalpost(game_obj)
    

    def apply_debuff_to_ball(self, ball: Ball):
        debuff = self.gen_rand_debuff()
        # Logic to apply debuff to ball
        # ...

    def apply_debuff_to_player(self, player: Player):
        debuff = self.gen_rand_debuff()
        if debuff == 'froze':
            current_speedx = player.get_speed_x()
            current_speedy = player.get_speed_y()
            new_speedx = current_speedx * 0
            new_speedy = current_speedy * 0
            player.set_speed_x(new_speedx)
            player.set_speed_y(new_speedy)

    def apply_debuff_to_goalpost(self, goalpost: Goalpost):
        debuff = self.gen_rand_debuff()
        if debuff == 'size_down':
            current_height = goalpost.get_height()
            new_height = current_height  - (current_height * 0.5)
            goalpost.set_height(new_height)
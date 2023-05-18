import random
import pygame
from Collectables import Collectables
from GameObject import GameObject
from Goalpost import Goalpost
from Ball import Ball
from Player import Player
class Buff(Collectables):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, duration: float, type: str):
        super().__init__(width, height, pos_x, pos_y,duration,type)

    # Generate a random buff for the match.
    def gen_rand_buff(self) -> str:
        buffs = ['speed_up', 'size_up']
        return random.choice(buffs)

    def apply_buff(self, game_obj: GameObject):
        if isinstance(game_obj, Ball):
            self.apply_buff_to_ball(game_obj)
        elif isinstance(game_obj, Player):
            self.apply_buff_to_player(game_obj)
        elif isinstance(game_obj, Goalpost):
            self.apply_buff_to_goalpost(game_obj)

    #def apply_buff_to_ball(self, ball: Ball):
        """ def apply_buff_to_player(self, player: Player):
        buff = self.gen_rand_buff()
        # Lógica para aplicar o buff ao jogador   """
    

    def apply_buff_to_goalpost(self, goalpost: Goalpost):
        buff = self.gen_rand_buff()
        if buff == 'size_up':
            current_height = goalpost.get_height()
            new_height = current_height * 1.5
            goalpost.set_height(new_height)
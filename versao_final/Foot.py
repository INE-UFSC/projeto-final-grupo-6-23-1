import pygame
from MovingObjects import MovingObjects
from utils import get_file_path
from Player import Player
from pygame import Rect, event
import Ball
from Goalpost import Goalpost
from CollisionList import CollisionList
from GameObject import GameObject
import math

#from what i've gathered the player's feet just collide with other players and with the ball

class Foot(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass: float, player: Player):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass)
        self.__player = player
        self.__controller = {
            "SPACE": pygame.K_SPACE
        }
        image_path = get_file_path('sprites', 'players', 'foot.png')
        self.__sprite = pygame.image.load(image_path)

    def move(self, events: event, game_objects: list[GameObject]):
        self.update_old_rect()

        for event in events:
            if event.type == KEYDOWN and event.key == self.__controller["SPACE"]:
                pass

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (self.__player.get_width(), self.__player.get_height()/4))
        surface.blit(resized_sprite, rect)
from MovingObjects import MovingObjects
from GameObject import GameObject
from Player import Player
import pygame
from pygame import Rect, event
from pygame.locals import *

class Ball(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, radius: int):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y)
        self.__radius = radius
        self.__retention = 0.7 # variable that retains ball momentum when bouncing
        self.__friction = 0.7 # ball friction against soil

    def handle_gravity(self, height, gravity):
        stop_bounce = 4 #value choosen by tests, subject to change
        speed_y = self.get_speed_y()
        
        if self.get_pos_y() + self.__radius < height:
            self.set_speed_y(speed_y + gravity)
        else:
            if speed_y > stop_bounce:
                self.set_speed_y(speed_y * -1 * self.__retention)
            elif abs(speed_y) <= stop_bounce:
                self.set_speed_y(0)

    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):
        for obj in game_objects:
            if isinstance(obj, Player):
                self.handle_player_collision(obj)

        #288 should be height parameter
        self.handle_friction(288)
        self.handle_gravity(288, gravity)
        self.handle_x_collision(width)

    def handle_friction(self, height):
        stop_rotating = 0.3

        if self.get_speed_y() == 0 and abs(self.get_speed_x()) < stop_rotating:
            self.set_speed_x(0)
        elif self.get_pos_y() + self.__radius >= height:
            self.set_speed_x(self.get_speed_x() * self.__friction)

    def handle_x_collision(self, width):
        speed_x = self.get_speed_x()
        
        if self.get_pos_x() + self.__radius < width and speed_x > 0:
            self.set_speed_x(speed_x)
        elif self.get_pos_x() + self.__radius > width and speed_x > 0:
            self.set_speed_x((speed_x) * -1)
        elif self.get_pos_x() + self.__radius > 0 and speed_x < 0:
            self.set_speed_x(speed_x)
        elif self.get_pos_x() + self.__radius < 0 and speed_x < 0:
            self.set_speed_x((speed_x) * -1)

    def handle_player_collision(self, player: Player):
        is_colliding = Rect.colliderect(self.get_rect(), player.get_rect())

        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        #improvements:
        #when bouncing against a player it should have some speed added to it based on the player's speed
        #some speed limit should be added, in order to avoid the ball bouncing like crazy
        if is_colliding:
            if speed_x < 1: #subject to change to interact with kicks
                self.set_speed_x(speed_x * -1 + player.get_speed_x() * 0.8)
            else:
                self.set_speed_x(speed_x * -1)
                self.set_speed_y(speed_y * -1)

    def update_pos(self):
        new_rect = Rect(self.get_pos_x() + self.get_speed_x(), 
                        self.get_pos_y() + self.get_speed_y(), 
                        self.get_rect().width,
                        self.get_rect().height
                    )
        self.set_rect(new_rect)

    def move(self, screen: pygame.Surface, game_objects: list[GameObject], gravity: float, **args):
        width = screen.get_width()
        height =  screen.get_height()
        self.check_collisions(width, height, game_objects, gravity)
        self.update_pos()

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 255, 255), self.get_rect())

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
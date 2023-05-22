from Character import Character
from pygame import Rect, event
import pygame
from pygame.locals import *
from utils import BUFF_APPLIED, DEBUFF_APPLIED
from GameObject import GameObject

class Player(Character):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass:float, controller: int):
        goals = 0
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass, goals)
        self.__controller = controller
        self.__default_speed = 10
        self.__default_jump_speed = 20

        # maybe create an object?
        self.__controllers = [
            {
                "UP": pygame.K_UP,
                "DOWN":  pygame.K_DOWN,
                "LEFT": pygame.K_LEFT,
                "RIGHT": pygame.K_RIGHT
            },
            {
                "UP": pygame.K_w,
                "DOWN":  pygame.K_s,
                "LEFT": pygame.K_a,
                "RIGHT": pygame.K_d
            },
        ]
        self.__is_buffed = False
        self.__is_debuffed = False
    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):
        for obj in game_objects:
            if isinstance(obj, Player) and obj != self:
                self.handle_player_collision(obj)
        
        self.collision_with_screen(width, height)

    def collision_with_screen(self, width, height):
        player = self.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()
        
        if player.right >= width and speed_x > 0:
            player.right = width
            self.set_speed_x(0)
        elif player.left <= 0 and speed_x < 0:
            player.left = 0
            self.set_speed_x(0)
        elif player.bottom >= height and speed_y >= 0:
            player.bottom = height
            self.set_speed_y(0)
        elif player.top <= 0 and speed_y < 0:
            player.top = 0
            self.set_speed_y(0)

    def handle_player_collision(self, other_player):
        player = self.get_rect()
        player2 = other_player.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        is_colliding = Rect.colliderect(player, player2)
        collision_tolerance = 20
        if is_colliding:
            if abs(player.top - player2.bottom) <= collision_tolerance and speed_y < 0:
                player.top = player2.bottom
                self.set_speed_y(0)
            if abs(player.right - player2.left) <= collision_tolerance and speed_x > 0:
                player.right = player2.left
                self.set_speed_x(0)
            if abs(player.bottom - player2.top) <= collision_tolerance and speed_y > 0:
                player.bottom = player2.top
                self.set_speed_y(0)
            if abs(player.left - player2.right) <= collision_tolerance and speed_x < 0:
                player.left = player2.right
                self.set_speed_x(0)

    def move(self, events: event, screen: pygame.Surface, game_objects: list[GameObject], gravity: float, **args):
        controller = self.__controllers[self.__controller]
        height = screen.get_height()
        player = self.get_rect()

        self.handle_gravity(height, gravity)

        for event in events:
            if event.type == KEYDOWN:
                if event.key == controller["UP"]:
                    self.set_speed_y(-self.__default_jump_speed)
                if event.key == controller["LEFT"]:
                    self.set_speed_x(-self.__default_speed)
                if event.key == controller["RIGHT"]:
                    self.set_speed_x(self.__default_speed)
            elif event.type == KEYUP:
                if event.key == controller["RIGHT"] and self.get_speed_x() > 0:
                    self.set_speed_x(0)
                elif event.key == controller["LEFT"] and self.get_speed_x() < 0:
                    self.set_speed_x(0)
        
        self.check_collisions(
            screen.get_width(), 
            screen.get_height(),
            game_objects,
            gravity
            )

        player.x += self.get_speed_x()
        player.y += self.get_speed_y()

    def handle_gravity(self, height, gravity):
        player = self.get_rect()
        speed_y = self.get_speed_y()

        if player.bottom < height: # 288 must be height param
            self.set_speed_y(speed_y + gravity)
        else:
            self.set_speed_y(0)

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 0, 0), self.get_rect())

    def handle_events(self, events: event):
        for event in events:
            if event.type == BUFF_APPLIED and not self.__is_buffed and self == event.target:
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height) * 1.5)
                self.set_rect(new_rect_applied)
                self.__is_buffed = True
        
            elif event.type == DEBUFF_APPLIED and not self.__is_debuffed and self == event.target:
                player_min = self.get_rect().height * 0.5
                new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min)
                self.set_rect(new_rect_debuff)
                self.__is_debuffed = True
       
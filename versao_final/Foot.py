from Character import Character
from pygame import Rect, event
import pygame
import Ball
from pygame.locals import *
from utils import BUFF_APPLIED, DEBUFF_APPLIED, RESET_STATE, get_file_path
from GameObject import GameObject
from Goalpost import Goalpost
from Scenario import Scenario
from CollisionList import CollisionList
from Player import Player
import math

class Foot(Character):
    def __init__(self, width: int, height: int, player: Player):
        goals = 0
        super().__init__(width, height, player.get_pos_x(), player.get_pos_y(), player.get_speed_x(), player.get_speed_y(), player.get_mass(), goals)
        self.__player = player
        self.__default_speed = 4
        self.__default_jump_speed = 4
        self.__is_player_one = player.get_player_one()
        self.__is_kicking = False
        self.__angle = 0
        self.__controller = player.get_controller()

        # Load image
        image_path = get_file_path('sprites', 'players', "foot.png")
        self.__sprite = pygame.image.load(image_path)

        # Inverts image horizontally if not player one (player in the left)
        if self.__is_player_one == False:
            self.__sprite = pygame.transform.flip(self.__sprite, True, False)

        # maybe create an object?
        self.__controllers = [
            {"SPACE": pygame.K_c},
            {"SPACE": pygame.K_SPACE}
        ]
    
    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):
        #update horizontal position and check for collisions
        self.update_pos('horizontal')
        self.handle_collision('horizontal', game_objects)

        #update vertical position and check for collisions
        #self.handle_gravity(height, gravity)
        self.update_pos('vertical')
        self.handle_collision('vertical', game_objects)
        
        self.collision_with_screen(width)

    def handle_collision(self, direction, game_objects):
        if direction == 'horizontal':
            collision_list = CollisionList(self, game_objects)

            for obj in collision_list.get_collisions():
                if isinstance(obj, Player) and obj != self:
                    ...
                    #self.handle_player_collision(obj, direction)
                elif isinstance(obj, Ball.Ball):
                    self.handle_ball_collision(obj, direction)

        elif direction == 'vertical':
            collision_list = CollisionList(self, game_objects)

            for obj in collision_list.get_collisions():
                if isinstance(obj, Player) and obj != self:
                    ...
                    #self.handle_player_collision(obj, direction)
                elif isinstance(obj, Goalpost):
                    self.handle_goalpost_collision(obj)
                elif isinstance(obj, Ball.Ball):
                    self.handle_ball_collision(obj, direction)

    def collision_with_screen(self, width):
        player = self.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        if player.right >= width and speed_x > 0:
            player.right = width
            self.set_speed_x(0)
        elif player.left <= 0 and speed_x < 0:
            player.left = 0
            self.set_speed_x(0)
        elif player.top <= 0 and speed_y < 0:
            player.top = 0
            self.set_speed_y(0)

    def handle_ball_collision(self, obj: Ball, direction):
        collision_strengh = 10
        player_rect = self.get_rect()
        player_old_rect = self.get_old_rect()

        ball_rect = obj.get_rect()
        ball_old_rect = obj.get_old_rect()

        if direction == 'horizontal':
            #collision on the right
            if player_rect.right >= ball_rect.left and player_old_rect.right <= ball_old_rect.left:
                player_rect.right = ball_rect.left
                obj.kick(self.get_speed_x(), collision_strengh, self.__player, 'x')

            #collision on the left
            if player_rect.left <= ball_rect.right and player_old_rect.left >= ball_old_rect.right:
                player_rect.left = ball_rect.right
                obj.kick(self.get_speed_x(), collision_strengh, self.__player, 'x')

        if direction == 'vertical':
            #collision on top
            if player_rect.top <= ball_rect.bottom and player_old_rect.top >= ball_old_rect.bottom:
                ball_rect.bottom = player_rect.top
                obj.kick(self.get_speed_y(), collision_strengh, self.__player, 'y')
                if self.get_speed_x() != 0:
                    obj.kick(self.get_speed_x(), collision_strengh, self.__player, 'x')

            #collision on bottom
            if player_rect.bottom >= ball_rect.top and player_old_rect.bottom <= ball_old_rect.top:
                player_rect.bottom = ball_rect.top

    def handle_goalpost_collision(self, goalpost: Goalpost):
        player = self.get_rect()
        player_old_rect = self.get_old_rect()
        goalpost_rect = goalpost.get_rect()
        
        if player.top <= goalpost_rect.top and player_old_rect.top > goalpost_rect.top:
            player.top = goalpost_rect.top
            self.set_speed_y(0)
        if player.bottom >= goalpost_rect.top and player_old_rect.bottom <= goalpost_rect.top:
            player.bottom = goalpost_rect.top
            self.set_speed_y(0)

    def move(self, events: event, screen: pygame.Surface, game_objects: list[GameObject], scenario: Scenario, gravity: float, **args):
        controller = self.__controllers[self.__controller]
        self.update_old_rect()

        for event in events:
            if event.type == KEYDOWN:
                if event.key == controller["SPACE"]:
                    self.__is_kicking = True
            elif event.type == KEYUP:
                if event.key == controller["SPACE"]:
                    self.__is_kicking = False
                    self.__angle = 0

        self.check_collisions(
            screen.get_width(), 
            screen.get_height(),
            game_objects,
            gravity
            )

    def update_pos(self, direction):
        x = self.get_pos_x()
        y = self.get_pos_y()
        if self.__is_kicking:
            if abs(x - self.__player.get_pos_x()) <= 75 and abs(y - self.__player.get_pos_y()) <= 75 and self.__angle <= 1.25:
                if self.__is_player_one:
                    self.set_speed_x(self.__default_speed*math.cos(self.__angle))
                else:
                    self.set_speed_x(-self.__default_speed*math.cos(self.__angle))
                self.set_speed_y(-self.__default_jump_speed*math.sin(self.__angle))

                self.__angle += 0.075

                speed_x = self.get_speed_x()
                speed_y = self.get_speed_y()

                self.set_pos(x+speed_x, y+speed_y)
            else:
                if self.__is_player_one:
                    self.set_pos(self.__player.get_pos_x()+51, self.__player.get_pos_y())
                else:
                    self.set_pos(self.__player.get_pos_x()-51,self.__player.get_pos_y())
        else:
            x = self.__player.get_pos_x()
            y = self.__player.get_pos_y()

            self.set_pos(x, y + self.__player.get_height())

    def handle_gravity(self, height, gravity):
        player = self.get_rect()
        speed_y = self.get_speed_y()

        if player.bottom < height: # 288 must be height param
            self.set_speed_y(speed_y + gravity)
        else:
            self.set_speed_y(0)

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

    def handle_events(self, events: event):
        for event in events:
            if event.type == BUFF_APPLIED  and event.collectable_type == 'size_up_player' and self.__player == event.target:
                height = self.get_rect().height
                self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height * 2))
                self.set_rect(new_rect_applied)
        
            elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'size_down_player' and self.__player == event.target:
                player_min = self.get_rect().height * 0.5
                new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min )
                self.set_rect(new_rect_debuff)

            #elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'fronzen' and self == event.target:

            if event.type == RESET_STATE and self.__player == event.target:
                if event.collectable_type == 'size_up_player':
                   self.get_rect().height *= 0.5 
                
                elif event.collectable_type == 'size_down_player':
                    height = self.get_rect().height
                    self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                    self.get_rect().height *=2

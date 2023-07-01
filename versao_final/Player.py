from Character import Character
from pygame import Rect, event
import pygame
import Ball
from pygame.locals import *
from utils import BUFF_APPLIED, DEBUFF_APPLIED, RESET_STATE, get_file_path
from GameObject import GameObject
from Ground import Ground
from Goalpost import Goalpost
from Scenario import Scenario
from CollisionList import CollisionList

class Player(Character):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass:float, controller: int, sprite: str, is_player_one: bool):
        goals = 0
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass, goals)
        self.__controller = controller
        self.__default_speed = 5
        self.__default_jump_speed = 8
        self.__in_floor = False
        self.__is_player_one = is_player_one
        self.__is_frozen = False

        # Load image
        image_path = get_file_path('sprites', 'players', sprite)
        self.__sprite = pygame.image.load(image_path)

        # Inverts image horizontally if not player one (player in the left)
        if self.__is_player_one == False:
            self.__sprite = pygame.transform.flip(self.__sprite, True, False)

        # maybe create an object?
        self.__controllers = [
            {
                "UP": pygame.K_w,
                "DOWN":  pygame.K_s,
                "LEFT": pygame.K_a,
                "RIGHT": pygame.K_d
            },
            {
                "UP": pygame.K_UP,
                "DOWN":  pygame.K_DOWN,
                "LEFT": pygame.K_LEFT,
                "RIGHT": pygame.K_RIGHT
            },
        ]
    
    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):
        #update horizontal position and check for collisions
        self.update_pos('horizontal')
        self.handle_collision('horizontal', game_objects)

        #update vertical position and check for collisions
        self.handle_gravity(height, gravity)
        self.update_pos('vertical')
        self.handle_collision('vertical', game_objects)
        
        self.collision_with_screen(width)

    def handle_collision(self, direction, game_objects):
        if direction == 'horizontal':
            collision_list = CollisionList(self, game_objects)

            for obj in collision_list.get_collisions():
                if isinstance(obj, Player) and obj != self:
                    self.handle_player_collision(obj, direction)
                elif isinstance(obj, Ball.Ball):
                    self.handle_ball_collision(obj, direction)

        elif direction == 'vertical':
            collision_list = CollisionList(self, game_objects)

            for obj in collision_list.get_collisions():
                if isinstance(obj, Player) and obj != self:
                    self.handle_player_collision(obj, direction)
                elif isinstance(obj, Ground):
                    self.handle_ground_collision(obj)
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
                obj.kick(self.get_speed_x(), collision_strengh, self, 'x')

            #collision on the left
            if player_rect.left <= ball_rect.right and player_old_rect.left >= ball_old_rect.right:
                player_rect.left = ball_rect.right
                obj.kick(self.get_speed_x(), collision_strengh, self, 'x')

        if direction == 'vertical':
            #collision on top
            if player_rect.top <= ball_rect.bottom and player_old_rect.top >= ball_old_rect.bottom:
                ball_rect.bottom = player_rect.top
                obj.kick(self.get_speed_y(), collision_strengh, self, 'y')
                if self.get_speed_x() != 0:
                    obj.kick(self.get_speed_x(), collision_strengh, self, 'x')

            #collision on bottom
            if player_rect.bottom >= ball_rect.top and player_old_rect.bottom <= ball_old_rect.top:
                player_rect.bottom = ball_rect.top
                self.__in_floor = True

    def handle_player_collision(self, other_player, direction):
        player = self.get_rect()
        player_old_rect = self.get_old_rect()
        player2 = other_player.get_rect()
        player2_old_rect = other_player.get_old_rect()

        if direction == 'horizontal':
            if player.right >= player2.left and player_old_rect.right <= player2_old_rect.left:
                player.right = player2.left
            if player.left <= player2.right and player_old_rect.left >= player2_old_rect.right:
                player.left = player2.right
        elif direction == 'vertical':
            if player.top <= player2.bottom and player_old_rect.top >= player2_old_rect.bottom:
                player.top = player2.bottom
                self.set_speed_y(0)
            if player.bottom >= player2.top and player_old_rect.bottom <= player2_old_rect.top:
                player.bottom = player2.top
                self.__in_floor = True
                self.set_speed_y(0)

    def handle_ground_collision(self, ground: Ground):
        player = self.get_rect()
        player_old_rect = self.get_old_rect()
        ground_rect = ground.get_rect()
        
        if player.bottom >= ground_rect.top and player_old_rect.bottom <= ground_rect.top:
            player.bottom = ground_rect.top
            self.set_speed_y(0)
            self.__in_floor = True

    def handle_goalpost_collision(self, goalpost: Goalpost):
        player = self.get_rect()
        player_old_rect = self.get_old_rect()
        goalpost_rect = goalpost.get_rect()
        
        if player.top <= goalpost_rect.top and player_old_rect.top > goalpost_rect.top:
            player.top = goalpost_rect.top
            self.set_speed_y(0)
        if player.bottom >= goalpost_rect.top and player_old_rect.bottom <= goalpost_rect.top:
            player.bottom = goalpost_rect.top
            self.__in_floor = True
            self.set_speed_y(0)

    def move(self, events: event, screen: pygame.Surface, game_objects: list[GameObject], scenario: Scenario, gravity: float, **args):
        controller = self.__controllers[self.__controller]
        self.update_old_rect()

        if not self.__is_frozen:
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == controller["UP"] and self.__in_floor == True:
                        self.set_speed_y(-self.__default_jump_speed)
                        self.__in_floor = False
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

    def update_pos(self, direction):
        x = self.get_pos_x()
        y = self.get_pos_y()

        if direction == 'horizontal':
            speed = self.get_speed_x()
            self.set_pos(x + speed, y)
        elif direction == 'vertical':
            speed = self.get_speed_y()
            self.set_pos(x, y + speed)

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
            if event.type == BUFF_APPLIED  and event.collectable_type == 'size_up_player' and self == event.target:
                height = event.target.get_rect().height
                self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height * 2))
                self.set_rect(new_rect_applied)
        
            elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'size_down_player' and self == event.target:
                player_min = self.get_rect().height * 0.5
                new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min )
                self.set_rect(new_rect_debuff)

            elif event.type == DEBUFF_APPLIED  and event.collectable_type == 'frozen_player' and self == event.target:
                self.__is_frozen = True
                        

            if event.type == RESET_STATE and self == event.target:
                if event.collectable_type == 'size_up_player':
                   event.target.get_rect().height *= 0.5 
                
                elif event.collectable_type == 'size_down_player':
                    height = event.target.get_rect().height
                    self.set_pos(self.get_pos_x(), self.get_pos_y() - height) 
                    event.target.get_rect().height *=2
                
                elif event.collectable_type == 'frozen_player':
                    self.__is_frozen = False
                    
    def get_player_one(self):
        return self.__is_player_one
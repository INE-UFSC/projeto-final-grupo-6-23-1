from Character import Character
from pygame import Rect, event
import pygame
from pygame.locals import *
from utils import BUFF_APPLIED, DEBUFF_APPLIED, RESET_STATE, get_image_path
from GameObject import GameObject
from Ground import Ground
from Goalpost import Goalpost
from Scenario import Scenario

class Player(Character):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass:float, controller: int, sprite: str, is_player_one: bool):
        goals = 0
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass, goals)
        self.__controller = controller
        self.__default_speed = 10
        self.__default_jump_speed = 20
        self.__in_floor = False

        # Load image
        image_path = get_image_path('sprites', 'players', sprite)
        self.__sprite = pygame.image.load(image_path)

        # Inverts image horizontally if not player one (player in the left)
        if is_player_one == False:
            self.__sprite = pygame.transform.flip(self.__sprite, True, False)

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
    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):
        for obj in game_objects:
            if isinstance(obj, Player) and obj != self:
                self.handle_player_collision(obj)
            if isinstance(obj, Ground):
                self.handle_ground_collision(obj)
            if isinstance(obj, Goalpost):
                self.handle_goalpost_collision(obj)
        
        self.collision_with_screen(width)

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

    def handle_ground_collision(self, ground: Ground):
        player = self.get_rect()
        ground_rect = ground.get_rect()

        is_colliding = Rect.colliderect(player, ground_rect)
        collision_tolerance = 20
        if is_colliding:
            if abs(player.bottom - ground_rect.top) <= collision_tolerance:
                player.bottom = ground_rect.top
                self.set_speed_y(0)
                self.__in_floor = True

    def handle_goalpost_collision(self, goalpost: Goalpost):
        player = self.get_rect()
        goalpost_rect = goalpost.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()
        collision_tolerance = 20

        is_colliding = Rect.colliderect(goalpost_rect, player)
        if is_colliding:
            if abs(player.top - goalpost_rect.bottom) <= collision_tolerance:
                player.top = goalpost_rect.bottom
                self.set_speed_y(0)
            if abs(player.right - goalpost_rect.left) <= collision_tolerance:
                player.right = goalpost_rect.left
                self.set_speed_x(0)
            if abs(player.bottom - goalpost_rect.top) <= collision_tolerance:
                player.bottom = goalpost_rect.top
                self.set_speed_y(0)
            if abs(player.left - goalpost_rect.right) <= collision_tolerance:
                player.left = goalpost_rect.right
                self.set_speed_x(0)

    def move(self, events: event, screen: pygame.Surface, game_objects: list[GameObject], scenario: Scenario, gravity: float, **args):
        controller = self.__controllers[self.__controller]
        height = screen.get_height() - scenario.get_ground_height()
        player = self.get_rect()

        self.handle_gravity(height, gravity)

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

        player.x += self.get_speed_x()
        player.y += self.get_speed_y()

    def handle_gravity(self, height, gravity):
        player = self.get_rect()
        speed_y = self.get_speed_y()

        if player.bottom < height: # 288 must be height param
            self.set_speed_y(speed_y + gravity)
        else:
            self.set_speed_y(0)

    def draw(self, pg: pygame, surface: pygame.Surface, r: int, g: int, b: int):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

    def handle_events(self, events: event):
        for event in events:
            if event.type == BUFF_APPLIED  and self == event.target:
                new_rect_applied = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, (self.get_rect().height * 2))
                self.set_rect(new_rect_applied)
        
            elif event.type == DEBUFF_APPLIED  and self == event.target:
                player_min = self.get_rect().height * 0.5
                new_rect_debuff = Rect(self.get_pos_x(),self.get_pos_y(),self.get_rect().width, self.get_rect().height - player_min )
                self.set_rect(new_rect_debuff)

            if event.type == RESET_STATE and self == event.target:
                if event.collectable_type == 'size_up_player':
                   event.target.get_rect().height *= 0.5 
                
                elif event.collectable_type == 'size_down_player':
                    event.target.get_rect().height *=2

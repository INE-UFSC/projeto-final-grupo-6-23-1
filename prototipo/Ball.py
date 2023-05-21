from MovingObjects import MovingObjects
from GameObject import GameObject
from Player import Player
import pygame
from pygame import Rect, event
from pygame.locals import *

class Ball(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass: float, radius: int):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass)
        self.__radius = radius
        self.__retention = 0.7 # variable that retains ball momentum when bouncing
        self.__friction = 0.7 # ball friction against soil
        self.last_touched_player = None

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

        self.collision_with_screen(width, height)

    def collision_with_screen(self, width, height):
        ball = self.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()
        
        if ball.right >= width and speed_x > 0:
            ball.right = width
            self.set_speed_x(speed_x * -1)
        elif ball.left <= 0 and speed_x < 0:
            ball.left = 0
            self.set_speed_x(speed_x * -1)
        elif ball.bottom >= height and speed_y >= 0:
            ball.bottom = height
            self.set_speed_y(speed_y * -1)
        elif ball.top <= 0 and speed_y < 0:
            ball.top = 0
            self.set_speed_y(speed_y * -1)

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

    def calc_final_velocity(self, ball_speed, player_speed):
        delta_t = 0.1 # collision time
        ball_mass = self.get_mass()
        ball_a = (ball_speed + player_speed) / delta_t
        f_ball = ball_mass * ball_a
        fv_ball = ((f_ball * delta_t) + (ball_mass * ball_speed))/ball_mass

        return fv_ball

    def handle_player_collision(self, player: Player):
        ball = self.get_rect()
        player_rect = player.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        is_colliding = Rect.colliderect(player_rect, ball)
        collision_tolerance = 20
        
        fv_ball_y = self.calc_final_velocity(speed_y, player.get_speed_y())
        fv_ball_x = self.calc_final_velocity(speed_x, player.get_speed_x())

        if is_colliding:
            if abs(ball.top - player_rect.bottom) <= collision_tolerance:
                ball.top = player_rect.bottom
                self.set_speed_y(fv_ball_y)
            if abs(ball.right - player_rect.left) <= collision_tolerance:
                ball.right = player_rect.left
                self.set_speed_x(fv_ball_x)
            if abs(ball.bottom - player_rect.top) <= collision_tolerance:
                ball.bottom = player_rect.top
                self.set_speed_y(fv_ball_y)
            if abs(ball.left - player_rect.right) <= collision_tolerance:
                ball.left = player_rect.right
                self.set_speed_x(fv_ball_x)
            self.last_touched_player = player
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

        self.handle_friction(height)
        self.handle_gravity(height, gravity)
        self.check_collisions(width, height, game_objects, gravity)
        self.update_pos()

    def draw(self, pg: pygame, surface: pygame.Surface):
        pg.draw.rect(surface, (255, 255, 255), self.get_rect())

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def handle_events(self,events):
        pass

    def set_pos(self, pos_x: int, pos_y: int):
        super().set_pos(pos_x, pos_y)
        self.set_speed_x(0)
        self.set_speed_y(0)

from MovingObjects import MovingObjects
from GameObject import GameObject
from Goalpost import Goalpost
from Ground import Ground
import pygame
import Player # needs to be imported like this, otherwise an error is thrown
from CollisionList import CollisionList
from pygame import Rect, event
from pygame.locals import *
from utils import get_file_path

class Ball(MovingObjects):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, mass: float):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y, mass)
        self.__retention = 0.7 # variable that retains ball momentum when bouncing
        self.__friction = 0.95 # ball friction against soil
        self.__last_touched_player = None
        self.__stop_bounce = 3
        self.__in_ground = False
        self.__goal = False

        #Note: Ball should not goes as faster as the player.width/2, this can cause
        #the ball to tunneling
        self.__speed_limit = 15

        # Load image
        image_path = get_file_path('sprites', 'ball.png')
        self.__sprite = pygame.image.load(image_path)

    def handle_gravity(self, gravity):
        if self.__in_ground is not True:
            speed_y = self.get_speed_y()
            self.set_speed_y(speed_y + gravity)

    def handle_stop_bounce(self, limiter, allow_in_ground_update = True):
        speed_y = self.get_speed_y()
        ball = self.get_rect()

        if abs(speed_y) > self.__stop_bounce:
            self.set_speed_y(speed_y * self.__retention)
        elif abs(speed_y) <= self.__stop_bounce and ball.bottom <= limiter:
            self.set_speed_y(0)
            if allow_in_ground_update:
                self.__in_ground = True

    def check_collisions(self, width: int, height: int, game_objects: list[GameObject], gravity: float):        
        self.update_pos('horizontal')
        self.collision_with_screen(width, height, 'horizontal')
        self.handle_friction() 
        self.handle_collision('horizontal', game_objects)
        
        self.update_pos('vertical')
        self.collision_with_screen(width, height, 'vertical')
        self.handle_gravity(gravity)
        self.handle_collision('vertical', game_objects)

    def handle_collision(self, direction, game_objects):
        if direction == 'horizontal':
            collision_list = CollisionList(self, game_objects)
            
            for obj in collision_list.get_collisions():
                if isinstance(obj, Player.Player):
                    self.handle_player_collision(obj, direction)
                elif isinstance(obj, Goalpost):
                    self.handle_goalpost_collision(obj, direction)
                    self.__goal = True

        elif direction == 'vertical':
            collision_list = CollisionList(self, game_objects)

            for obj in collision_list.get_collisions():
                if isinstance(obj, Player.Player):
                    self.handle_player_collision(obj, direction)
                elif isinstance(obj, Ground):
                    self.handle_ground_collision(obj)
                elif isinstance(obj, Goalpost):
                    self.handle_goalpost_collision(obj, direction)

    def collision_with_screen(self, width, height, direction):
        ball = self.get_rect()
        ball_old_rect = self.get_old_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()
        
        if direction == 'horizontal':
            if ball.right >= width and ball_old_rect.right <= width:
                ball.right = width
                self.set_speed_x(speed_x * -1)
            elif ball.left <= 0 and ball_old_rect.left >= 0:
                ball.left = 0
                self.set_speed_x(speed_x * -1)
        elif direction == 'vertical':
            if ball.bottom >= height and ball_old_rect.bottom <= height:
                ball.bottom = height
                self.set_speed_y(speed_y * -1)
            elif ball.top <= 0 and ball_old_rect.top >= 0:
                ball.top = 0

    def handle_friction(self):
        stop_rotating = 0.3
        
        if abs(self.get_speed_x()) < stop_rotating:
            self.set_speed_x(0)
        elif self.__in_ground:
            self.set_speed_x(self.get_speed_x() * self.__friction)

    def handle_player_collision(self, obj, direction):
        ball_speed_x = self.get_speed_x()
        ball_speed_y = self.get_speed_y()
        ball_rect = self.get_rect()
        ball_old_rect = self.get_old_rect()

        player_rect = obj.get_rect()
        player_old_rect = obj.get_old_rect()
        self.__last_touched_player = obj

        if direction == 'horizontal':
            #collision on the right
            if ball_rect.right >= player_rect.left and ball_old_rect.right <= player_old_rect.left:
                ball_rect.right = player_rect.left
                self.set_speed_x(ball_speed_x * -1)

            #collision on the left
            elif ball_rect.left <= player_rect.right and ball_old_rect.left >= player_old_rect.right:
                ball_rect.left = player_rect.right
                self.set_speed_x(ball_speed_x * -1)

        if direction == 'vertical':
            #collision on the right
            if ball_rect.bottom <= player_rect.top and ball_old_rect.bottom >= player_old_rect.top:
                ball_rect.bottom = player_rect.top

            #collision on the left
            elif ball_rect.top >= player_rect.bottom and ball_old_rect.top <= player_old_rect.bottom:
                ball_rect.top = player_rect.bottom

            self.set_speed_y(ball_speed_y * -1)

    def handle_goalpost_collision(self, goalpost: Goalpost, direction):
        ball_rect = self.get_rect()
        ball_old_rect = self.get_old_rect()
        goalpost_rect = goalpost.get_rect()
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        if direction == 'horizontal':
            if ball_rect.top <= goalpost_rect.top and ball_rect.bottom >= goalpost_rect.top:
                if ball_rect.right >= goalpost_rect.left and ball_old_rect.right <= goalpost_rect.left:
                    ball_rect.right = goalpost_rect.left
                    self.set_speed_x((speed_x) * -1)
                if ball_rect.left <= goalpost_rect.right and ball_old_rect.left >= goalpost_rect.right:
                    ball_rect.left = goalpost_rect.right
                    self.set_speed_x((speed_x) * -1)
        elif direction == 'vertical':
            if ball_rect.bottom >= goalpost_rect.top and ball_old_rect.bottom <= goalpost_rect.top:
                ball_rect.bottom = goalpost_rect.top
                self.set_speed_y(speed_y * -1)
                self.handle_stop_bounce(goalpost_rect.top, False)
                #when ball is stuck above goalposts it gains some speed to not get stuck
                if self.get_speed_x() == 0:
                    if goalpost.get_side() == 'right':
                        self.set_speed_x(-1)
                    elif goalpost.get_side() == 'left':
                        self.set_speed_x(1)

    def handle_ground_collision(self, ground: Ground):
        ball_rect = self.get_rect()
        ball_old_rect = self.get_old_rect()
        ground_rect = ground.get_rect()
        ground_old_rect = ground.get_old_rect()
        speed_y = self.get_speed_y()

        if ball_rect.bottom >= ground_rect.top and ball_old_rect.bottom <= ground_old_rect.top:
            ball_rect.bottom = ground_rect.top
            self.set_speed_y(speed_y * -0.75)
            self.handle_stop_bounce(ground_rect.top)

    def get_last_touched(self):
        return self.__last_touched_player
    
    def update_pos(self, direction):
        x = self.get_pos_x()
        y = self.get_pos_y()

        if direction == 'horizontal':
            speed = self.get_speed_x()
            self.set_pos(x + speed, y)
        elif direction == 'vertical':
            speed = self.get_speed_y()
            self.set_pos(x, y + speed)

    #ensures ball does not goes faster than expected
    def apply_speed_limiter(self):
        speed_x = self.get_speed_x()
        speed_y = self.get_speed_y()

        if abs(speed_x) >= self.__speed_limit:
            self.set_speed_x((speed_x/abs(speed_x)) * self.__speed_limit)
        if abs(speed_y) >= self.__speed_limit:
            self.set_speed_y((speed_y/abs(speed_y)) * self.__speed_limit)
    
    def kick(self, speed, collision_strengh, player):

        self.__last_touched_player = player
        #values of collision strengh subject to change
        if speed > 0:
            self.set_speed_x(collision_strengh)
        elif speed < 0:
            self.set_speed_x(-collision_strengh)

    def move(self, screen: pygame.Surface, game_objects: list[GameObject], gravity: float, **args):
        width = screen.get_width()
        height =  screen.get_height()
        self.update_old_rect()

        self.check_collisions(width, height, game_objects, gravity)
        self.apply_speed_limiter()

    def draw(self, pg: pygame, surface: pygame.Surface):
        rect = self.get_rect()
        resized_sprite = pygame.transform.scale(self.__sprite, (rect.width, rect.height))
        surface.blit(resized_sprite, rect)

    def set_goal(self, goal: bool):
        self.__goal = goal

    def get_goal(self):
        return self.__goal

    def set_in_ground(self, in_ground: bool):
        self.__in_ground = in_ground

    def handle_events(self,events):
        pass
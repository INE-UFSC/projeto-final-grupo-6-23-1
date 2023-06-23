import pygame
from pygame.locals import *
from GameObject import GameObject
from Player import Player
from Ball import Ball
from MovingObjects import MovingObjects
from Collectables import Collectables
from Buff import Buff
from Debuff import Debuff
from Goalpost import Goalpost
from Scenario import Scenario
from Ground import Ground
import random
from utils import *

class Match:
    def __init__(self, surface):
        self.__scenario: Scenario = Scenario()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(get_file_path('sprites', 'sound', 'crowd_sound.wav'))
        pygame.mixer.music.play(-1)
        self.__game_objects: list[GameObject] = [
            Player(40, 50, 270, self.__scenario.get_ground_height(), 0, 0, 50, 0, sprite='messi.png', is_player_one=False),
            Player(40, 50, 350, self.__scenario.get_ground_height(), 0, 0, 50, 1, sprite='ronaldinho.png', is_player_one=True),
            Ball(20, 20, 310, self.__scenario.get_ground_height(), 0, 0, 1.5),
            #Debuff(20,20, 150, 50, 10),
            #Buff(20,20,400,50,10),
            Goalpost(*self.__get_goal_params(surface, 'left')),
            Goalpost(*self.__get_goal_params(surface, 'right')),
            *self.__scenario.get_structures()
        ]
        self.__time: int = 180
        self.__gravity = 0.6
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.time.set_timer(CREATE_COLLECTABLE, 5000)
        #self.__collectable_timer = 10

    """ def check_collisions(self):
        for game_obj in self.__game_objects:
            game_obj.check_collisions(self.__game_objects) """

    def draw_time(self):
        font = pygame.font.Font(None, 40)
        if self.__time >= 0:
            text = font.render(str(self.__time), False, 'White')
        else:
            text = font.render('Time Up!', False, 'White')
            #pygame.quit()
        return text

    def draw_score(self):
        scores = self.update_score()
        font = pygame.font.Font(None, 40)
        text_player1 = font.render(str(scores[0]), False, 'White')
        text_player2 = font.render(str(scores[1]), False, 'White')
        return [text_player1, text_player2]

    def process_input(self, events, screen):
        for obj in self.__game_objects:
            if isinstance(obj, MovingObjects):
                obj.move(
                    events= events, 
                    screen= screen, 
                    game_objects= self.__game_objects,
                    scenario = self.__scenario,
                    gravity= self.__gravity
                )
            elif isinstance(obj, Collectables):
                obj.check_collision(self.__game_objects)

            obj.handle_events(events)
    

    def draw(self, pg: pygame, surface: pygame.Surface):
        surface.fill((0, 0, 0)) #it clears the previous frame to draw a new one
        """ background = pygame.image.load(get_image_path('sprites','stages','test','background.png'))
        ground = pygame.image.load(get_image_path('sprites','stages','test','ground.png'))
        surface.blit(background, (0,0))
        surface.blit(ground, (0,288)) """

       # print("---------------")
        #print(len(self.__game_objects))
        #print(self.__game_objects)
        for obj in self.__game_objects:
            if isinstance(obj, Player):
                if self.__game_objects.index(obj) == 0:
                    obj.draw(pg, surface, 0, 255 , 255)
                else:
                    obj.draw(pg, surface, 255, 255 , 0)
            else:
                obj.draw(pg, surface)


        surface.blit(self.draw_time(), (300,5))

        surface.blit(self.draw_score()[0], (0, 5))
        surface.blit(self.draw_score()[1], (615, 5))

    def check_goal(self):
        #can be implemented with custom event, ex
        """
        suppose that the event is called GOAL, and it's implemented as such:
            GOAL = pygame.USEREVENT + 1

            it can be send to the events list in pygame using:
            ev = pygame.event.Event(GOAL)
            pygame.event.post(ev)

            then check_goal() can receive events and then handle the pygame event GOAL
        """
        pass

    # calcs initial Goalpost parameters
    # gp = which goalpost -> 'left' or 'right'
    def __get_goal_params(self, surface, gp):
        goal_height = 120
        goal_width = 60
        goal_y = surface.get_height() - self.__scenario.get_ground_height() - goal_height
        goal_x = 0
        if gp == 'right':
            goal_x = surface.get_width() - goal_width

        return goal_width, goal_height, goal_x, goal_y

    def handle_events(self, events, surface):
        for event in events:
            if event.type == pygame.USEREVENT:
                self.update_time()
            elif event.type == CREATE_COLLECTABLE:
                self.create_rand_collectable(surface)

    def update_time(self):
        self.__time -= 1

    def update_score(self):
        for obj in self.__game_objects:
            if isinstance(obj, Ball):
                if obj.get_goal() == True:
                    if obj.get_pos_x() <= 128:
                        self.__game_objects[0].add_goals()
                        self.reset()
                    elif obj.get_pos_x() >= 532:
                        self.__game_objects[1].add_goals()
                        self.reset()

        score_player1 = self.__game_objects[0].get_goals()
        score_player2 = self.__game_objects[1].get_goals()
        if score_player1==7 or score_player2==7:
            #pygame.quit()
            pass
        return [score_player1, score_player2]
    
    def reset(self):
        self.__game_objects[0].set_pos(270, 0)
        self.__game_objects[1].set_pos(350, 0)
        self.__game_objects[2].set_pos(310, 0)
        self.__game_objects[2].set_goal(False)
        self.__game_objects[2].set_in_ground(False)
        self.__game_objects[2].set_speed_x(0)
        self.__game_objects[2].set_speed_y(0)
    
    def create_rand_collectable(self,surface):
        collectables_count = sum(isinstance(obj, Collectables) for obj in self.__game_objects)
        if collectables_count >= 3:
            return
        chose_collectable = collectables_count % 2
        new_collectable = None
        if chose_collectable == 0:
            buff_type = Buff.gen_rand_buff()
            new_collectable = Buff(20,20,0,0,10,buff_type)
        else:
            debuff_type = Debuff.gen_rand_debuff()
            new_collectable = Debuff(20,20,0,0,10,debuff_type)
        new_collectable.set_to_random_position(self.__game_objects, screen=surface)
        self.__game_objects.append(new_collectable)

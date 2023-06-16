import pygame
from pygame import Rect
from utils import get_image_path

class Scenario:
    def __init__(self, surface):
        self.__ground_image = pygame.image.load(get_image_path('sprites','stages','test','ground.png'))
        self.__image: list[list] = ['          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    '          ',
                                    'gggggggggg']
        self.__ground_rects, self.__wall_rects = self.create_rects(surface)

    def create_rects(self, surface: pygame.Surface):
        height = surface.get_height()
        width = surface.get_width()

        rect_h = height/len(self.__image)
        rect_w = width/len(self.__image[0])
        ground_rects = []
        walls = []
        for index, line in enumerate(self.__image):
            for n_col, column in enumerate(line):
                if column == "g":
                    pos_x = n_col * rect_w
                    pos_y = index * rect_h 
                    new_ground = Rect(pos_x, pos_y, rect_w, rect_h)
                    ground_rects.append(new_ground)
                elif column == 'w':
                    pos_x = n_col * rect_w
                    pos_y = n_col * rect_h 
                    new_wall = Rect(pos_x, pos_y, rect_w, rect_h)
                    walls.append(new_wall)

        return ground_rects, walls

    def draw(self, surface):
        for ground in self.__ground_rects:
            resized_sprite = pygame.transform.scale(self.__ground_image, (ground.width, ground.height))
            surface.blit(resized_sprite, ground)
        for wall in self.__wall_rects:
            pygame.draw.rect(surface, (255, 255, 255), wall)

    def get_ground_rects(self):
        return self.__ground_rects
    
    def get_wall_rects(self):
        return self.__wall_rects
    
    def get_ground_height(self):
        return self.__ground_rects[0].height
    


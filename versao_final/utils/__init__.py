import os
import inspect
from GameObject import GameObject
import pygame
from pygame.locals import *

BUFF_APPLIED = USEREVENT + 1
DEBUFF_APPLIED = USEREVENT + 2
RESET_STATE = USEREVENT + 3
CREATE_COLLECTABLE = USEREVENT + 4

def get_obj_of_type(obj_list: list[GameObject], obj_type) -> list:
    found_objs = []
    for obj in obj_list:
        if isinstance(obj, obj_type):
            found_objs.append(obj)

    return found_objs

def get_image_path(*args):
    # Get the address of the calling file
    calling_frame = inspect.stack()[1]
    calling_module = inspect.getmodule(calling_frame[0])
    calling_file_dir = os.path.dirname(os.path.abspath(calling_module.__file__))

    path = [calling_file_dir, *args]
    image_path = os.path.join(*path)

    return image_path
from ..GameObject import GameObject

def get_obj_of_type(obj_list: list[GameObject], obj_type) -> list:
    found_objs = []
    for obj in obj_list:
        if isinstance(obj, obj_type):
            found_objs.append(obj)

    return found_objs
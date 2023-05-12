class GameObject:
    def __init__(self, width, height, pos_x, pos_y):
        self.__width = width
        self.__height = height
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    # getters and setters
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_pos_x(self) -> int:
        return self.__pos_x
    
    def get_pos_y(self) -> int:
        return self.__pos_y
    
    def set_width(self, witdh: int):
        self.__width = witdh

    def set_height(self, height: int):
        self.__height = height

    def set_pos_x(self, pos_x: int):
        self.__pos_x = pos_x

    def set_pos_y(self, pos_y: int):
        self.__pos_y = pos_y
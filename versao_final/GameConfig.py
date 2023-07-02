class GameConfig:

    def __init__(self):
        #iniciate with default values
        self.__map = 'default'
        self.__screen_width = 640
        self.__screen_height = 360
        self.__fps = 60

    def set_map(self, map: str):        
        if self.__map == 'default':
            self.__map = 'desert'

        elif self.__map == 'desert':
            self.__map = 'default'
            
    def set_screen_width(self, width: str):
        self.__screen_width = width

    def set_screen_height(self, height: str):
        self.__screen_height = height

    def set_fps(self, fps):
        self.__fps = fps

    def get_map(self):
        return self.__map
    
    def get_screen_width(self):
        return self.__screen_width
    
    def get_screen_height(self):
        return self.__screen_height
    
    def get_fps(self):
        return self.__fps
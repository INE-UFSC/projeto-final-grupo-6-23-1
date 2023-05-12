from Character import Character

class Player(Character):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float):
        goals = 0 
        super.__init__(self, width, height, pos_x, pos_y, speed_x, speed_y, goals)

    def move(self):
        pass
from GameObject import GameObject
from Ball import Ball
class Goalpost(GameObject):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int):
        super().__init__(width, height, pos_x, pos_y)

    def check_goal(self, ball: Ball) -> bool:
        if self.get_rect().colliderect(ball.get_rect()):
            return True
        else:
            return False
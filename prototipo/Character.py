from abc import ABC
from MovingObjects import MovingObjects
class Character(MovingObjects, ABC):
    def __init__(self, width: int, height: int, pos_x: int, pos_y: int, speed_x: float, speed_y: float, goals: int = 0):
        super().__init__(width, height, pos_x, pos_y, speed_x, speed_y)
        self.__goals = goals

    def get_goals(self) -> int:
        return self.__goals

    def add_goals(self) -> None:
        self.__goals += 1
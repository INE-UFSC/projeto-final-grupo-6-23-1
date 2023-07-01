import PySimpleGUI as sg
from utils import get_file_path

class New_Game:

    def __init__(self):
        self.__players = [
            get_file_path('sprites', 'players', 'messi.png'),
            get_file_path('sprites', 'players', 'ronaldinho.png'),
        ]
        
        self.__match = [
            get_file_path('sprites', 'stages', 'stadium.png'),
            get_file_path('sprites', 'stages', 'desert.png'),
        ]

        self.__vector = 0
        self.__select = self.__players[self.__vector]
        self.__vector_match = 0
        self.__select_match = self.__match[self.__vector_match]
        sg.theme('Default 1')
        self.__buttons_new_game = [
            [sg.Text((""), pad=(0,20))],
            [sg.Button("NEXT", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(705, 0))], [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(707, 25))]
        ]

        self.__layout_new_game = [
        [sg.Text(("PRE MATCH"), font=('Comic Sans MS', 40), pad=(605,30))],
        [sg.Text(("PLAYER 1"), font=('Comic Sans MS', 30), pad=(200,15)), sg.Text((""), font=('Comic Sans MS', 30), pad=(255,10)), sg.Text(("PLAYER 2"), font=('Comic Sans MS', 30), pad=(90,25))],
        [sg.Text((""), font=('Comic Sans MS', 24), pad=(105,25)), sg.Button("⬅️", key="-PREV-", font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 42)), sg.Image(filename=self.__select, key="-IMAGE-", pad=(10,27)), sg.Button("➡️", key="-NEXT" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 30)), sg.Text((""), pad=(75,0)),sg.Button("⬅️", key="-PREVIOUS" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 0)), sg.Image(filename=self.__select_match, key="-GAME-", pad=(15,0)),sg.Button("➡️", key="-FOLLOWING" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 50)),sg.Text("", pad=(90,0)), sg.Button("⬅️", key="-HOME-", font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 42)), sg.Image(filename=self.__select, key="-IMAGE_UNIFORM-", pad=(10,0)), sg.Button("➡️", key="-END" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 0))],
        *self.__buttons_new_game,
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_new_game,finalize=True)
        self.__window.Maximize()
        
    def close(self):
        self.__window.close()
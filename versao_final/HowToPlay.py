import PySimpleGUI as sg
from utils import get_file_path

class HowToPlay:
    
    def __init__(self):

        sg.theme('Default 1')

        self.__layout_how_to_play = [
                [sg.Text(("CONTROLS"), font=('Comic Sans MS', 30), pad=(645,50), text_color=('black'))],
                [sg.Text(("PLAYER 1"), font=('Comic Sans MS', 30), pad=(350,35), text_color=('black')), sg.Text(("PLAYER 2"), font=('Comic Sans MS', 30), pad=(100,0), text_color=('black'))],
                [sg.Image(filename=get_file_path('keyboard', 'W.png'), pad=(415,0))],
                [sg.Text((""), pad=(173,0)), sg.Image(filename=get_file_path('keyboard', 'A.png'), pad=(0,0)), sg.Image(filename=get_file_path('keyboard', 'S.png'), pad=(0,0)),sg.Image(filename=get_file_path('keyboard', 'D.png'), pad=(0,0)),sg.Text((''), pad=(210,0)) ,sg.Image(filename=get_file_path('keyboard', 'HOME.png'), pad=(0,0)) ,sg.Image(filename=get_file_path('keyboard', 'PGUP&PGDN.png'), pad=(0,0)),sg.Image(filename=get_file_path('keyboard', 'END.png'), pad=(0,0))],
                [sg.Image(filename=get_file_path('keyboard', 'C.png'), pad=(416,30)),sg.Image(filename=get_file_path('keyboard', 'SPACE.png'), pad=(0,0))],
                [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(710, 40))]
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_how_to_play, size=(800,600), finalize=True)
        self.__window.Maximize()

    def close(self):
        self.__window.close()
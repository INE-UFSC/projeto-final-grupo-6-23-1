import PySimpleGUI as sg

class HowToPlay:
    
    def __init__(self):

        sg.theme('Default 1')

        self.__layout_how_to_play = [
                [sg.Text(("CONTROLS"), font=('Comic Sans MS', 30), pad=(645,50), text_color=('black'))],
                [sg.Text(("PLAYER 1"), font=('Comic Sans MS', 30), pad=(350,35), text_color=('black')), sg.Text(("PLAYER 2"), font=('Comic Sans MS', 30), pad=(100,0), text_color=('black'))],
                [sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//W.png", pad=(415,0))],
                [sg.Text((""), pad=(173,0)), sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//A.png", pad=(0,0)), sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//S.png", pad=(0,0)),sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//D.png", pad=(0,0)),sg.Text((''), pad=(210,0)) ,sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//HOME.png", pad=(0,0)) ,sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//PGUP&PGDN.png", pad=(0,0)),sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//END.png", pad=(0,0))],
                [sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//P.png", pad=(416,30)),sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//KEYBOARD//SPACE.png", pad=(0,0))],
                [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(710, 40))]
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_how_to_play, size=(800,600), finalize=True)
        self.__window.Maximize()
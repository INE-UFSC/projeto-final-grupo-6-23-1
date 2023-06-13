from Pre_Match import Pre_Match
import PySimpleGUI as sg

class NewGame:
    def __init__(self):
        pass
   
        sg.theme('Default 1')
        self.__buttons_new_game = [
            [sg.Button("PLAY AGAINST THE COMPUTER", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(515, 55))],
            [sg.Button("PLAY 1 VS 1", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(657, 20))],
            [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(697, 55))]
        ]

        self.__layout_new_game = [
                [sg.Text("CHOOSE AN OPTION BELOW:", font=('Comic Sans MS', 40), pad=(360,45))],
                *self.__buttons_new_game
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_new_game, size=(800, 600),finalize=True)
        self.__window.Maximize()
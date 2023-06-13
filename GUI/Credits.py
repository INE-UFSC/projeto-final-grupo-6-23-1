import PySimpleGUI as sg

class Credits:
    def __init__(self):

        sg.theme('Default 1')

        self.__layout_credits = [
            [sg.Text(("CREDITS"), font=('Comic Sans MS', 40), pad=(635,75), text_color=('black'))],
            [sg.Text(("ARTHUR DE LARA MACHADO"), font=('Comic Sans MS', 22), pad=(550,15), text_color=('black'))],
            [sg.Text(("ANDRÉ THIAGO PFLEGER"), font=('Comic Sans MS', 22), pad=(570,15), text_color=('black'))],
            [sg.Text(("CAIO FERREIRA CARDOSO"), font=('Comic Sans MS', 22), pad=(560,15), text_color=('black'))],
            [sg.Text(("FELIPE FAGUNDES PACHECO"), font=('Comic Sans MS',22), pad=(545,15), text_color=('black'))],
            [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(700, 50))],
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_credits, size=(800,600),finalize=True)
        self.__window.Maximize()
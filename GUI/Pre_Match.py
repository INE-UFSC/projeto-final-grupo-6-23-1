import PySimpleGUI as sg

class Pre_Match:

    def __init__(self, real_opponent):
        self.__real_opponent = real_opponent
        self.__players = [
            "C://Users//User//Desktop//projeto_final_poo_2//projeto-final-grupo-6-23-1//versao_final//sprites//players//messi.png",
            "C://Users//User//Desktop//projeto_final_poo_2//projeto-final-grupo-6-23-1//versao_final//sprites//players//ronaldinho.png"
        ]
        self.__vector = 0
        self.__select = self.__players[self.__vector]
        sg.theme('Default 1')
        self.__buttons_Pre_Match = [
            [sg.Text((""), pad=(0,50))],
            [sg.Button("NEXT", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(700, 0))], [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(702, 25))]
        ]
        
        if self.__real_opponent == False:
            opponent = sg.Text(("COMPUTER"), font=('Comic Sans MS', 30), pad=(70,25))
        else:
            opponent = sg.Text(("PLAYER 2"), font=('Comic Sans MS', 30), pad=(90,25))

        self.__layout_Pre_Match = [
        [sg.Text(("UNIFORM COLORS"), font=('Comic Sans MS', 30), pad=(565,40))],
        [sg.Text(("PLAYER 1"), font=('Comic Sans MS', 30), pad=(200,15)), sg.Text((""), font=('Comic Sans MS', 30), pad=(255,10)), opponent],
        [sg.Image(filename=self.__players[0], pad=(250,0))],
        *self.__buttons_Pre_Match,
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_Pre_Match,finalize=True)
        self.__window.Maximize()
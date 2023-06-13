import PySimpleGUI as sg

class Pre_Match:

    def __init__(self, real_opponent):
        self.__real_opponent = real_opponent
        self.__uniforms_color = [
            "C://Users//User//Desktop//ARQUIVOS//Shirts//Camisa_Verde.png",
            "C://Users//User//Desktop//ARQUIVOS//Shirts//Camisa_Azul.png",
            "C://Users//User//Desktop//ARQUIVOS//Shirts//Camisa_Vermelha.png"
        ]
        self.__vector = 0
        self.__select = self.__uniforms_color[self.__vector]
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
        [sg.Text((""), font=('Comic Sans MS', 24), pad=(100,25)), sg.Button("⬅️", key="-PREV-", font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 42)), sg.Image(filename=self.__select, key="-IMAGE-", pad=(10,27)), sg.Button("➡️", key="-NEXT" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 30)), sg.Text((""), pad=(80,0)),sg.Button("⬅️", key="-PREVIOUS" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 0)), sg.Image(filename=r"C://Users//User//Desktop//ARQUIVOS//Cenario//background.png", pad=(34,0)),sg.Button("➡️", key="-FOLLOWING" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 50)),sg.Text("", pad=(106,0)), sg.Button("⬅️", key="-HOME-", font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 42)), sg.Image(filename=self.__select, key="-IMAGE_UNIFORM-", pad=(10,0)), sg.Button("➡️", key="-END" ,font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(0, 0))],
        [sg.Text((""), font=('Comic Sans MS', 24), pad=(100,0)), sg.Image(filename="C://Users//User//Desktop//ARQUIVOS//Cenario//ground.png", pad=(405,0))],
        *self.__buttons_Pre_Match,
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout_Pre_Match,finalize=True)
        self.__window.Maximize()
        
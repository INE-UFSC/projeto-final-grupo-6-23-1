import PySimpleGUI as sg

class Text:
    def __init__(self):
        sg.theme('Default 1')
        self.__buttons = [
            [sg.Button("BACK", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(700, 80))]
        ]

        self.__layout = [
            [sg.Text(("ABOUT THE GAME"), font=('Comic Sans MS', 40), pad=(500,70))],
            [sg.Text(("      WELCOME TO THE EXCITING WORLD OF 2D FOOTBALL! HERE, THE VICTORY IS "), font=('Comic Sans MS', 20), pad=(117,10))],
            [sg.Text("DETERMINED BY THE TEAM THAT SCORED THE MOST GOALS IN A PERIOD OF 5 MINUTES.", font=('Comic Sans MS', 20), pad=(117,10))],
            [sg.Text("IN CASE OF A TIE, GET READY FOR THE EXCITING 'GOLDEN GOAL'.", font=('Comic Sans MS', 20), pad=(260,10))],
            [sg.Text("HAVE FUN AND BE THE CHAMPION OF THIS ADRENALINE-FILLED GAME!", font=('Comic Sans MS', 20), pad=(230,10))],
            [sg.Column(self.__buttons, element_justification="center", vertical_alignment="center")],        
        ]
        self.__window = sg.Window('GOAL MASTERS', self.__layout, size=(800,600),finalize=True)
        self.__window.Maximize()

    def close(self):
        self.__window.close()
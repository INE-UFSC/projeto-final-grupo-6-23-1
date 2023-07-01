import PySimpleGUI as sg

class Restart:
    def __init__(self):
        sg.theme('Default 1')
        self.__buttons = [
            [sg.Button("RESTART", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 25))],
            [sg.Button("BACK TO MENU", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 25))]
        ]

        self.__layout = [
            [sg.Text("END GAME", font=('Comic Sans MS', 40), pad=(610,100))],            
            [sg.Column(self.__buttons, element_justification="center", vertical_alignment="center")]
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout, size=(800,600),finalize=True)
        self.__window.Maximize()
        event, values = self.__window.read()
    
    def close(self):
        self.__window.close()
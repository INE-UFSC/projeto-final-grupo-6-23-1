import PySimpleGUI as sg

class HowToPlay:
    
    def __init__(self):

        sg.theme('Default 1')

        self.__layout_how_to_play = [
                [sg.Text((""), font=('Jokerman', 30), pad=(290,35), text_color=('black'))],
                [sg.Text((""), font=('Jokerman', 12), pad=(270,15), text_color=('black'))],
                [sg.Text((""), font=('Jokerman', 12), pad=(270,15), text_color=('black'))],
                [sg.Button("VOLTAR", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(330, 15))]
        ]


        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == "VOLTAR":
                self.window.close()

            
    def close(self):
        self.window.close()




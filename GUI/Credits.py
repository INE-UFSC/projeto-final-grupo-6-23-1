import PySimpleGUI as sg

class Credits:
    def __init__(self):

        sg.theme('Default 1')

        self.layout_credits = [
            [sg.Text(("CREDITS"), font=('Jokerman', 30), pad=(290,35), text_color=('black'))],
            [sg.Text(("ARTHUR DE LARA MACHADO"), font=('Jokerman', 12), pad=(270,15), text_color=('black'))],
            [sg.Text(("ANDRÉ THIAGO PFLEGER"), font=('Jokerman', 12), pad=(270,15), text_color=('black'))],
            [sg.Text(("CAIO FERREIRA CARDOSO"), font=('Jokerman', 12), pad=(270,15), text_color=('black'))],
            [sg.Text(("FELIPE FAGUNDES PACHECO"), font=('Jokerman',12), pad=(270,15), text_color=('black'))],
            [sg.Button("VOLTAR", font=('Comic Sans MS', 12), button_color=('black', '#FFB90F'), pad=(340, 25))],
        ]

        self.window = sg.Window('GOAL MASTERS', self.layout_credits, size=(800,600))

 
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == "VOLTAR":
                self.window.close()
                
            
            

    def close(self):
        self.window.close()

credits = Credits()


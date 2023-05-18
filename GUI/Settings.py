import PySimpleGUI as sg

class Settings:
    def __init__(self):
        sg.theme('Default 1')

        self.__buttons = [
            [sg.Button("VOLTAR", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(325, 225))]

        ]

        self.__layout_settings = [
            [sg.Frame(layout=[
                [sg.Radio('ON ', "MUSIC RADIO", default=True, size=(10, 1)), sg.Radio('OFF', "MUSIC RADIO")]], title='MUSIC',
                title_color='red', relief=sg.RELIEF_SUNKEN)],
            [sg.Text("", font=('Jokerman', 10), pad=(10, 25))],
            [sg.Frame(layout=[
                [sg.Radio('3 MINUTES ', "TIME GAME RADIO", default=True, size=(10, 1)), sg.Radio('5 MINUTES ', "TIME GAME RADIO", default=True, size=(10, 1)), sg.Radio('8 MINUTES', "TIME GAME RADIO")]], title='TIME GAME',
                title_color='red', relief=sg.RELIEF_SUNKEN)],
            
            [sg.Text("", font=('Jokerman', 10), pad=(10, 25))],
            [sg.Frame(layout=[
                [sg.Radio('FULL ', "SCREEN RADIO", default=True, size=(10, 1)), sg.Radio('REDUCED', "SCREEN RADIO")]], title='SCREEN SIZE',
                title_color='red', relief=sg.RELIEF_SUNKEN)],
            *self.__buttons,  # Desempacota o layout do botão na lista principal  
        ]

        self.window = sg.Window('GOAL MASTERS', self.__layout_settings, size=(800, 600))

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == "VOLTAR":
                self.window.close()

    def close(self):
        self.window.close()

settings = Settings()
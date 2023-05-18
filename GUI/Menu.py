import PySimpleGUI as sg
import pygame
import threading
from Credits import Credits

class Menu:
    def __init__(self):
 
        sg.theme('Default 1')
        
        self.buttons = [
            [sg.Button("NEW GAME", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(305, 15))],
            [sg.Button("PLAY 1v1", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(305, 15))],
            [sg.Button("HOW TO PLAY", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(305, 15))],
            [sg.Button("SETTINGS", font=('Jokerman',12), button_color=('black', '#FFB90F'), pad=(305,15))],
            [sg.Button("CREDITS", font=('Jokerman', 12), button_color=('black', '#FFB90F'), pad=(305, 15))],

        ]

        self.layout = [
            [sg.Text("GOAL MASTERS", font=('Jokerman', 20), pad=(250,45))],
            [sg.Column(self.buttons, element_justification="center", vertical_alignment="center"),]
        ]

        self.window = sg.Window('GOAL MASTERS', self.layout, size=(800,600))

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == "NEW GAME":
                print("new game") #A ser feito
            elif event == "PLAY 1v1":
                print("play 1v1") #A ser Feito
            elif event == "HOW TO PLAY":
                print("how to play") #A ser feito
            elif event == "SETTINGS":
                print("settings")

            elif event == "CREDITS":
                credits = Credits()
                
        self.window.close()

menu = Menu()
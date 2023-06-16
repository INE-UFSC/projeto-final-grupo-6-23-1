import PySimpleGUI as sg
from Credits import Credits
from HowToPlay import HowToPlay
from New_Game import New_Game
from Text import Text
import pygame


class Menu:
    def __init__(self):
        self.__pause = False
        sg.theme('Default 1')
        self.__buttons = [
            [sg.Button("NEW GAME", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 15))],
            [sg.Button("HOW TO PLAY", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 15))],
            [sg.Button("CREDITS", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 15))],
            [sg.Button("QUIT", font=('Comic Sans MS', 22), button_color=('black', '#FFB90F'), pad=(635, 15))]
        ]

        self.__layout = [
            [sg.Text("", font=('Comic Sans MS', 40), pad=(705,0)), sg.Button("⚽", font=('Comic Sans MS', 14), button_color=('black', '#FFB90F'), pad=(5, 15)), sg.Button("🔊", key="music_button", font=('Comic Sans MS', 14), button_color=('black', '#FFB90F'), pad=(5, 15))],
            [sg.Text("GOAL MASTERS", font=('Comic Sans MS', 44), pad=(520,45))],
            [sg.Column(self.__buttons, element_justification="center", vertical_alignment="center")],        
        ]

        self.__window = sg.Window('GOAL MASTERS', self.__layout, size=(800,600),finalize=True)
        self.__window.Maximize()
        
    def play_music(self): 
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\User\Desktop\projeto_final_poo_2\projeto-final-grupo-6-23-1\GUI\Extras\MusicaFundo.wav")
        pygame.mixer.music.play()

    def start(self):
        self.play_music()

    def close(self):
        self.__window.close()
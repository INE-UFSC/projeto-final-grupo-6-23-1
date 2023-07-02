import PySimpleGUI as sg
from Menu import Menu
from Credits import Credits
from HowToPlay import HowToPlay
from New_Game import New_Game
from Text import Text
from Game import Game
import pygame
from Restart import Restart
from GameConfig import GameConfig
from utils import get_file_path

class Global:
    def __init__(self):
        self.__screens = [Menu, Credits, HowToPlay, New_Game,Text,"END", Restart]
        self.__screen_actually = self.__screens[0]

    def events(self):
        self.__reproducing_music = False
        menu = Menu()
        while True:

            if self.__screen_actually == self.__screens[0]:
                if self.__reproducing_music == False:
                    menu.play_music()
                    menu.start()
                    self.__reproducing_music = True

                event, values = menu._Menu__window.read()

                if event == "NEW GAME":
                    menu._Menu__window.close()
                    new_game = New_Game()
                    event, values = new_game._New_Game__window.read()
                    self.__screen_actually = self.__screens[3]

                elif event == "HOW TO PLAY":
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[2]

                elif event == "CREDITS":
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[1]

                elif event == "music_button":
                    if menu._Menu__pause == False:
                        pygame.mixer.music.pause()
                        menu._Menu__pause = True
                        menu._Menu__window['music_button'].update(text=" 🔈 ")
                    else:
                        pygame.mixer.music.unpause()
                        menu._Menu__pause = False
                        menu._Menu__window['music_button'].update(text="🔊")
                
                elif event == "⚽":
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[4]

                elif event == "QUIT" or event == sg.WIN_CLOSED:
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[5]


            elif self.__screen_actually == self.__screens[1]:
                credits = Credits() 
                event, values = credits._Credits__window.read()
                if event == sg.WIN_CLOSED:
                    credits._Credits__window.close()
                    self.__screen_actually = self.__screens[7]

                elif event == "BACK":
                    credits._Credits__window.close()
                    self.__screen_actually = self.__screens[0]
                    menu = Menu()

            elif self.__screen_actually == self.__screens[2]:
                how_to_play = HowToPlay()
                event, values = how_to_play._HowToPlay__window.read()
                if event == sg.WIN_CLOSED:
                    how_to_play._HowToPlay__window.close()
                    self.__screen_actually = self.__screens[5]

                elif event == "BACK":
                    how_to_play._HowToPlay__window.close()
                    self.__screen_actually = self.__screens[0]
                    menu = Menu()

            elif self.__screen_actually == self.__screens[4]:
                text = Text()
                event, values = text._Text__window.read()

                if event == "BACK":
                    text._Text__window.close()
                    self.__screen_actually = self.__screens[0]
                    menu = Menu()

                elif event == sg.WIN_CLOSED:
                    self.__screen_actually = self.__screens[5]


            elif self.__screen_actually == self.__screens[3]:
                event, values = new_game._New_Game__window.read()

                if event == "BACK":
                    new_game._New_Game__window.close()
                    self.__screen_actually = self.__screens[0]
                    menu = Menu()

                elif event == "-PREV-":
                    if new_game._New_Game__vector == 0:
                        new_game._New_Game__vector = len(new_game._New_Game__players) - 1
                        new_game._New_Game__select = new_game._New_Game__players[new_game._New_Game__vector]
                        new_game._New_Game__window["-IMAGE-"].update(filename=new_game._New_Game__select)
                    else:
                        new_game._New_Game__vector -= 1
                        new_game._New_Game__select = new_game._New_Game__players[new_game._New_Game__vector]
                        new_game._New_Game__window["-IMAGE-"].update(filename=new_game._New_Game__select)

                elif event == "-NEXT":
                    if new_game._New_Game__vector == len(new_game._New_Game__players) - 1:
                        new_game._New_Game__vector = 0
                        new_game._New_Game__select = new_game._New_Game__players[new_game._New_Game__vector]
                        new_game._New_Game__window["-IMAGE-"].update(filename=new_game._New_Game__select)
                    else:
                        new_game._New_Game__vector += 1
                        new_game._New_Game__select = new_game._New_Game__players[new_game._New_Game__vector]
                        new_game._New_Game__window["-IMAGE-"].update(filename=new_game._New_Game__select)

                elif event == "-HOME-":
                    if new_game._New_Game__vector_2 == 0:
                        new_game._New_Game__vector_2 = len(new_game._New_Game__players_2) - 1
                        new_game._New_Game__select_2 = new_game._New_Game__players_2[new_game._New_Game__vector_2]
                        new_game._New_Game__window["-IMAGE_UNIFORM-"].update(filename=new_game._New_Game__select_2)
                    else:
                        new_game._New_Game__vector_2 -= 1
                        new_game._New_Game__select_2 = new_game._New_Game__players_2[new_game._New_Game__vector_2]
                        new_game._New_Game__window["-IMAGE_UNIFORM-"].update(filename=new_game._New_Game__select_2)

                elif event == "-END":
                    if new_game._New_Game__vector_2 == len(new_game._New_Game__players_2) - 1:
                        new_game._New_Game__vector_2 = 0
                        new_game._New_Game__select_2 = new_game._New_Game__players_2[new_game._New_Game__vector_2]
                        new_game._New_Game__window["-IMAGE_UNIFORM-"].update(filename=new_game._New_Game__select_2)
                    else:
                        new_game._New_Game__vector_2 += 1
                        new_game._New_Game__select_2 = new_game._New_Game__players_2[new_game._New_Game__vector_2]
                        new_game._New_Game__window["-IMAGE_UNIFORM-"].update(filename=new_game._New_Game__select_2)

                elif event == "-PREVIOUS":
                    if new_game._New_Game__vector_match == 0:
                        new_game._New_Game__vector_match = len(new_game._New_Game__match) - 1
                        new_game._New_Game__select_match = new_game._New_Game__match[new_game._New_Game__vector_match]
                        new_game._New_Game__window["-GAME-"].update(filename=new_game._New_Game__select_match)
                    else:
                        new_game._New_Game__vector_match -= 1
                        new_game._New_Game__select_match = new_game._New_Game__match[new_game._New_Game__vector_match]
                        new_game._New_Game__window["-GAME-"].update(filename=new_game._New_Game__select_match)

                elif event == "-FOLLOWING":
                    if new_game._New_Game__vector_match == len(new_game._New_Game__match) - 1:
                        new_game._New_Game__vector_match = 0
                        new_game._New_Game__select_match = new_game._New_Game__match[new_game._New_Game__vector_match]
                        new_game._New_Game__window["-GAME-"].update(filename=new_game._New_Game__select_match)
                    else:
                        new_game._New_Game__vector_match += 1
                        new_game._New_Game__select_match = new_game._New_Game__match[new_game._New_Game__vector_match]
                        new_game._New_Game__window["-GAME-"].update(filename=new_game._New_Game__select_match)

                elif event == "NEXT":
                    new_game._New_Game__window.close()
                    game_config = GameConfig()                   
                    game = Game(GameConfig())

                    if new_game._New_Game__vector_match == 0:
                        game._Game__config.set_map('default')

                    elif new_game._New_Game__vector_match == 1:
                        game._Game__config.set_map('desert')
                    
                    if game._Game__config.get_map == 'desert':
                        game._Game__config.set_sound(get_file_path('sprites', 'sound', 'crowd_sound.wav'))

                    elif game._Game__config.get_map == 'default':
                        game._Game__config.set_sound(get_file_path('sprites', 'sound', 'wind_sound.wav'))
                    game.start_game()
                          
                elif event == sg.WIN_CLOSED:
                    self.__screen_actually = self.__screens[5]
        
            elif self.__screen_actually == self.__screens[5]:
                break
                
            elif self.__screen_actually == self.__screen[6]:
                event, values = restart._Restart__window.read()
                if event == "RESTART":
                    restart._Restart__window.close()
                    new_game = Game(GameConfig())
                    new_game.start_game()
                    
                    new_game.start_game()

                elif event == "BACK TO MENU":
                    restart._Restart__window.close()
                    self.__screen_actually = self.__screens[0]
                    menu = Menu()
                                
start_game = Global()
start_game.events()
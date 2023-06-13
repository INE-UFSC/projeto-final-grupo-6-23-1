import PySimpleGUI as sg
from Menu import Menu
from Credits import Credits
from HowToPlay import HowToPlay
from NewGame import NewGame
from Text import Text
from Pre_Match import Pre_Match
import pygame

class Global:
    def __init__(self):
        self.__screens = [Menu, Credits, HowToPlay, NewGame,Text, "Pre_Match_True", "Pre_Match_False", "END"]
        self.__screen_actually = self.__screens[0]

    def events(self):
        self.__reproducing_music = False
        while True:

            if self.__screen_actually == self.__screens[0]:
                menu = Menu()
                if self.__reproducing_music == False:
                    menu.play_music()
                    menu.start()
                    self.__reproducin_music = True

                event, values = menu._Menu__window.read()

                if event == "NEW GAME":
                    new_game = NewGame()
                    event, values = new_game._NewGame__window.read()
                    menu._Menu__window.close()
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
                        menu._Menu__window['music_button'].update(text="🔈")
                    else:
                        pygame.mixer.music.unpause()
                        menu._Menu__pause = False
                        menu._Menu__window['music_button'].update(text="🔊")
                
                elif event == "⚽":
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[4]

                elif event == "QUIT" or event == sg.WIN_CLOSED:
                    menu._Menu__window.close()
                    self.__screen_actually = self.__screens[7]


            elif self.__screen_actually == self.__screens[1]:
                credits = Credits() 
                event, values = credits._Credits__window.read()
                if event == sg.WIN_CLOSED:
                    credits._Credits__window.close()
                    self.__screen_actually = self.__screens[7]

                elif event == "BACK":
                    credits._Credits__window.close()
                    self.__screen_actually = self.__screens[0] 

            elif self.__screen_actually == self.__screens[2]:
                how_to_play = HowToPlay()
                event, values = how_to_play._HowToPlay__window.read()
                if event == sg.WIN_CLOSED:
                    how_to_play._HowToPlay__window.close()
                    self.__screen_actually = self.__screens[7]

                elif event == "BACK":
                    how_to_play._HowToPlay__window.close()
                    self.__screen_actually = self.__screens[0]
            
            elif self.__screen_actually == self.__screens[3]:
                
                if event == sg.WIN_CLOSED:
                    self.__screen_actually = self.__screens[7]

                elif event == "BACK":
                    self.__screen_actually = self.__screens[0]
                    new_game._NewGame__window.close()

                elif event == "PLAY AGAINST THE COMPUTER":
                    self.__screen_actually = self.__screens[6]
                    new_game._NewGame__window.close()

                elif event == "PLAY 1 VS 1":
                    self.__screen_actually = self.__screens[5]
                    new_game._NewGame__window.close()

            elif self.__screen_actually == self.__screens[4]:
                text = Text()
                event, values = text._Text__window.read()

                if event == "BACK":
                    text._Text__window.close()
                    self.__screen_actually = self.__screens[0]

                elif event == sg.WIN_CLOSED:
                    self.__screen_actually = self.__screens[7]


            elif self.__screen_actually == self.__screens[5]:
                play_vs_play = Pre_Match(True)
                event, values = play_vs_play._Pre_Match__window.read()

                if event == "BACK":
                    play_vs_play._Pre_Match__window.close()
                    self.__screen_actually = self.__screens[3]
                elif event == "-PREV-":
                    if play_vs_play._Pre_Match__vector == 0:
                        play_vs_play._Pre_Match__vector = len(play_vs_play.__uniforms_color) - 1
                    else:
                        play_vs_play._Pre_Match__vector -= 1
                        
                    play_vs_play._Pre_Match__select = play_vs_play.__uniforms_color[play_vs_play.__vector]
                    play_vs_play._Pre_Match__window["-IMAGE-"].update(filename=play_vs_play.__select)

                elif event == "-NEXT":
                    if play_vs_play._Pre_Match__vector == len(play_vs_play._Pre_Match__uniforms_color) - 1:
                        play_vs_play._Pre_Match__vector = 0
                    else:
                        play_vs_play._Pre_Match__vector += 1
                        play_vs_play._Pre_Match__select = play_vs_play._Pre_Match__uniforms_color[play_vs_play._Pre_Match__vector]
                        play_vs_play._Pre_Match__window["-IMAGE-"].update(filename=play_vs_play._Pre_Match__select)

                elif event == "-HOME-":
                    if play_vs_play._Pre_Match__vector == 0:
                        play_vs_play._Pre_Match__vector = len(play_vs_play._Pre_Match__uniforms_color) - 1
                    else:
                        play_vs_play._Pre_Match__vector -= 1
                        play_vs_play._Pre_Match__select = play_vs_play._Pre_Match__uniforms_color[play_vs_play._Pre_Match__vector]

                elif event == "-END":
                    if play_vs_play._Pre_Match__vector == len(play_vs_play._Pre_Match__uniforms_color) - 1:
                        play_vs_play._Pre_Match__vector = 0
                    else:
                        play_vs_play._Pre_Match__vector += 1
                        play_vs_play._Pre_Match__select = play_vs_play._Pre_Match__uniforms_color[play_vs_play._Pre_Match__vector]
                        play_vs_play._Pre_Match__window["-IMAGE_UNIFORM-"].update(filename=play_vs_play._Pre_Match__select)

                elif event == "-PREVIOUS":
                    print("")
                elif event == "-FOLLOWING":
                    print("")

                elif event == "NEXT":
                    print("")  
            elif self.__screen_actually == self.__screens[6]:
                play_vs_computer = Pre_Match(False)
            
                event, values = play_vs_computer._Pre_Match__window.read()

                if event == "BACK":
                    play_vs_computer._Pre_Match__window.close()
                    self.__screen_actually = self.__screens[3]
                elif event == "-PREV-":
                    if play_vs_computer._Pre_Match__vector == 0:
                        play_vs_computer._Pre_Match__vector = len(play_vs_computer._Pre_Match__uniforms_color) - 1
                    else:
                        play_vs_computer._Pre_Match__vector -= 1
                        play_vs_computer._Pre_Match__select = play_vs_computer._Pre_Match__uniforms_color[play_vs_computer._Pre_Match__vector]
                        play_vs_computer._Pre_Match__window["-IMAGE-"].update(filename=play_vs_computer._Pre_Match__select)

                elif event == "-NEXT":
                    if play_vs_computer._Pre_Match__vector == len(play_vs_computer._Pre_Match__uniforms_color) - 1:
                        play_vs_computer._Pre_Match__vector = 0
                    else:
                        play_vs_computer._Pre_Match__vector += 1
                        play_vs_computer._Pre_Match__select = play_vs_computer._Pre_Match__uniforms_color[play_vs_computer._Pre_Match__vector]
                        play_vs_computer._Pre_Match__window["-IMAGE-"].update(filename=play_vs_computer._Pre_Match__select)

                elif event == "-HOME-":
                    if play_vs_computer._Pre_Match__vector == 0:
                        play_vs_computer._Pre_Match__vector = len(play_vs_computer._Pre_Match__uniforms_color) - 1
                    else:
                        play_vs_computer._Pre_Match__vector -= 1
                        play_vs_computer._Pre_Match__select = play_vs_computer._Pre_Match__uniforms_color[play_vs_computer._Pre_Match__vector]
                
                elif event == "-END":
                    if play_vs_computer._Pre_Match__vector == len(play_vs_computer._Pre_Match__uniforms_color) - 1:
                        play_vs_computer._Pre_Match__vector = 0
                    else:
                        play_vs_computer._Pre_Match__vector += 1
                        play_vs_computer._Pre_Match__select = play_vs_computer._Pre_Match__uniforms_color[play_vs_computer._Pre_Match__vector]
                        play_vs_computer._Pre_Match__window["-IMAGE_UNIFORM-"].update(filename=play_vs_computer._Pre_Match__select)
                elif event == "-PREVIOUS":
                    print("")
                elif event == "-FOLLOWING":
                    print("")

                elif event == "NEXT":
                    print("")
            elif self.__screen_actually == self.__screens[7]:
                break

a = Global()
a.events()
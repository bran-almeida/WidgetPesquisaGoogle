import PySimpleGUI as sg
import webbrowser
import speech_recognition as sr

class SearchWidget:

    def __init__(self):
        
        layout = [ [sg.Input(key='bar' ), sg.Button("Search", key='search')] ]
        window = sg.Window("Google Search", layout)
        while True:
            self.event, self.values = window.read()
            if self.event == "search":
                webbrowser.open_new_tab(f'www.google.com/search?q={self.values["bar"]}')
            if self.event == sg.WINDOW_CLOSED:
                break

SearchWidget()     
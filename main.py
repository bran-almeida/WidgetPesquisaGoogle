import PySimpleGUI as sg
import webbrowser
from time import sleep

class SearchWidget:

    def __init__(self):
        
        layout = [ [sg.Input(key='Search'), sg.Button("Search")] ]
        window = sg.Window("Google Search", layout)
        while True:
            self.event, self.values = window.read()
            if self.event == "Search0":
                webbrowser.open_new_tab(f'www.google.com/search?q={self.values["Search"]}')
            if self.event == sg.WINDOW_CLOSED:
                break

SearchWidget()
      
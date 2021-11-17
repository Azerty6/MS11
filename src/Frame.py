from tkinter import Frame, Label, Button, YES
from time import sleep
from src.DataInput import DataInput
from src.utils import present_xhi2_data


class Frame(Frame):

    def __init__(self, containeur, color):
        super().__init__(containeur, bg=color)
        """self.Title = None
        self.Subtitle = None
        self.Buttom = None
        self.Entry = []
        self.Canvas = None
        self.Bind = None"""
        self.elements = []

    def get_element(self, element):
        return self.elements[element]

    def add_element(self, element, **kw):
        element.pack(**kw)
        self.elements.append(element)
        return len(self.elements) - 1

    """
    def get_Title(self):
        return self.Title

    def get_Subtitle(self):
        return self.Subtitle

    def get_Buttom(self):
        return self.Buttom

    def get_Entry(self):
        return self.Entry

    def get_Canvas(self):
        return self.Canvas

    def get_Bind(self):
        return self.Bind
"""
    def add_text(self, content, police, size, background, forground):
        self.add_element(Label(self, text=content, font=(police, size), bg=background, fg=forground))

    def add_Button(self, content, police, size, background, forground, cmd):
        self.add_element(Button(self, text=content, font=(police, size), bg= background, fg=forground, command=cmd), pady=25)

    def add_Entry(self, entry):
        self.add_element(entry, expand=YES)

    def on_load(self, callback):
        self.bind("<Map>", callback)
    """
    def add_Bind(self, cmmd):
        self.Bind = bind(self, command=cmd)

    #def add_Canvas(self, content, police, size, background, forground):
      #  self.Title = tkinter.Canvas(self, text=content, front=(police, size), bg= background, fg=forground)

"""
    @classmethod
    def build_home(cls, window, callback):
        frame = Frame(window, "#4682B4")
        frame.add_text("Bienvenue sur le test du \u03C7\u00B2", "Arial", 35, '#4682B4', '#FFFFFF')
        frame.add_Button("Continuer", "Arial", 20, '#FFFFFF', '#4682B4', callback)
        frame.pack(expand=YES)
        return frame

    @classmethod
    def build_data_selection(cls, window, callback):

        frame = Frame(window, "#4682B4")
        frame.add_text(
            "Sélectionnez votre échantillons de mesures",
            "Arial", 18, '#4682B4', '#FFFFFF')
        frame.add_Button("Calculer", "Arial", 20, '#FFFFFF', '#4682B4', callback)
        data_input = DataInput(frame)
        frame.add_element(data_input)
        return frame, data_input

    @classmethod
    def build_table(cls, window, data_provider):
        frame = Frame(window, "#4682B4")
        frame.add_text("Tableau de \u03C7\u00B2", "Arial", 20, '#4682B4', '#FFFFFF')
        frame.on_load(lambda e: present_xhi2_data(data_provider()))
        return frame

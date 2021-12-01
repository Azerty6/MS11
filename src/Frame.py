import os
import statistics
from tkinter import Frame, Label, Button, YES
from time import sleep
from src.DataInput import DataInput
from src.utils import get_xhi2_data, display_data


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
        def import_values():
            data_input.clear()
            print(os.listdir())
            with open("../input/data", "r") as file:
                content = file.readlines()
                print(content)
                for i, line in enumerate(content):
                    data_input.entries[i].insert(0, line.replace("\n", ""))
                    data_input.generate_entry()
        frame = Frame(window, "#4682B4")
        frame.add_text(
            "Sélectionnez votre échantillons de mesures",
            "Arial", 18, '#4682B4', '#FFFFFF')
        frame.add_Button("Calculer", "Arial", 20, '#FFFFFF', '#4682B4', callback)
        frame.add_Button("Importer des valeurs (fichier input/data)", "Arial", 20, '#FFFFFF', '#4682B4', import_values)
        data_input = DataInput(frame)
        frame.add_element(data_input)
        return frame, data_input

    @classmethod
    def build_table(cls, window, data_provider):
        frame = Frame(window, "#4682B4")
        frame.add_text("Tableau de \u03C7\u00B2", "Arial", 20, '#4682B4', '#FFFFFF')
        def load(e):
            data = data_provider()
            class_data, xhi2, class_width, min_values, max_values, values, array_exp_freq = get_xhi2_data(data)
            frame.add_text("Classes :", "Arial", 15, "#4682B4", "#FFFFFF")
            frame.add_text("\n".join([str(class_) for class_ in class_data]), "Arial", 10, "#4682B4", "#FFFFFF")
            frame.add_text(f"\u03C7\u00B2 : {xhi2}", "Arial", 15, "#4682B4", "#FFFFFF")
            frame.add_text("Données random :", "Arial", 15, "#4682B4", "#FFFFFF")
            frame.add_text(f"Moyenne : {statistics.mean(data)}", "Arial", 10, "#4682B4", "#FFFFFF")
            frame.add_text(f"Ecart type : {statistics.stdev(data)}", "Arial", 10, "#4682B4", "#FFFFFF")
            display_data(class_width=class_width,
                         min_values=min_values,
                         max_values=max_values,
                         values=values,
                         array_exp_freq=array_exp_freq,
                data=data,
                mean=statistics.mean(data),
                std_dev=statistics.stdev(data),
                class_count=len(class_data),
                xhi2=xhi2
            )
        frame.on_load(load)
        return frame

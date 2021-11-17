import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
from src.DataArray import DataArray
from src.ClassData import ClassData
from src.Frame import Frame
from src.utils import present_xhi2_data

from tkinter import Tk, mainloop, Entry, YES

data = []


def ecart_centre_red(a, mean, ecart_type):
    b = (a - mean) / ecart_type
    return b

def population(a, b, data):
    pop = 0
    for value in data:
        if a <= value < b:
            pop += 1
    return pop


def home_buttom_continue():
    frame_home.destroy()
    frame_dataselection.pack(expand=YES)

def return_entry(en):
    content = Entry.get(en)
    print(content)
    return content


def get_data():
    return data


def data_buttom_calculate():

    #xhi2 = present_xhi2_data(data_input.get_data())
    #print(xhi2)

    #result = ("Valeurs centrées réduites : {}\nEtendue des valeurs : {}\nLongueur des classes : {}\nDonnées des classes : {}\nxhi² : {}".format(str(values), str(width), str(class_width), str(class_data), str(xhi2)))
    #print(result)

    #bins_class = []  # On definis les diffférents intervalles
    #for data in class_data:
    #    bins_class.append(data.infimum)
    #bins_class.append(values[-1])
    global data
    data = data_input.get_data()
    frame_dataselection.destroy()
    frame_table_presentation.pack()
    #list_calculate = (sample, sample_mean, Calculate_e_type_sb(), values, width, class_width, class_data, xhi2, bins_class)
    #print(list_calculate)
    #return list_calculate



window = Tk()

window.title("Test du \u03C7\u00B2")
window.geometry("720x480")
window.minsize(580, 300)
window.config(background='#4682B4')


frame_home = Frame.build_home(window, home_buttom_continue)
frame_dataselection, data_input = Frame.build_data_selection(window, data_buttom_calculate)
frame_table_presentation = Frame.build_table(window, lambda: data)


#total_rows = len(lst)
#total_columns = len(lst[0])



mainloop()
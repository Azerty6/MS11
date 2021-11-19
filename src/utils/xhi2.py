import statistics
import math
from src.ClassData import ClassData
from src.DataArray import DataArray
import matplotlib.pyplot as plt
import numpy as np


def population(a, b, data):
    pop = 0
    for value in data:
        if a <= value < b:
            pop += 1
    return pop


def compute_reduced_centered_vars(data):
    mean = statistics.mean(data)
    standard_deviation = statistics.stdev(data, mean)
    return sorted([(i - mean) / standard_deviation for i in data])


def position_in_integration_table(a):
    return str(a - a // 10 * 10), str(a // 100) + "." + str(a // 10 - a // 100 * 10)


def theorical_frequency(a, b, integration_table):
    # int(a < 0) = -1 si a > 0, 1 si a < 0
    # Les calculs sont bizarres, mais ils doivent marcher ^^
    a = abs(int(100 * a))
    b = abs(int(100 * b))
    pos_a = position_in_integration_table(a)
    pos_b = position_in_integration_table(b)
    return \
        (-1) ** int(a < 0) * float(integration_table[pos_a[1], pos_a[0]]) + \
        (-1) ** int(b > 0) * float(integration_table[pos_b[1], pos_b[0]])


def display_data(experimental_frequencies, data, mean, std_dev, class_count, xhi2):
    fig, ax = plt.subplots()  # On cree la fenetre pyplot
    exp_freq_array = np.array(experimental_frequencies)  # On change une liste en une matrice

    # 10,10,11,11,11,13,12,9,12,14
    # Echantillon test1
    x = []
    y = []
    # On cree une liste d'antécendant une une matrice d'immage pour pouvoir
    # creer la courbe théorique
    while len(x) <= 100:
        x.append((data[0] - mean) + len(x) * (data[-1] - data[0]) / 100)
    for i in range(len(x)):
        y.append((1 / (np.sqrt(2 * np.pi) * std_dev)) * np.exp(-0.5 * ((x[i]) / std_dev) ** 2))

    num_bins = class_count
    # On construit l'histogramme reel
    n, bins, patches = ax.hist(exp_freq_array, num_bins, density=True)
    # 14,15,16,17,18,14,15,17,16,17,17,18,17,17,13,15,15,15,14,13,16,17,18,14,15,16,17,18,19,17,14,17,16,15,15,16
    # echantillon test 2
    # 0.385,0.387,0.388,0.383,0.391,0.380,0.382,0.384,0,.386,0.389,0.390,0.385,0.389,0.388,0.382,0.387,0.388,0.392,0.383,0.388,0.385
    # 385,387,388,383,391,380,382,384,386,389,390,385,389,388,382,387,388,392,383,388,385
    # On transforme les liste en matrice
    x_array = np.array(x)
    y_array = np.array(y)
    # On met le teste de la bulle
    textstr = "$\mu=%.2f${}\n$\sigma=%.2f${}\n\u03C7\u00B2={}".format(round(mean, 3), round(std_dev, 3),
                                                                      round(xhi2, 4))
    # On creer la bulle
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # On assemble le texte et la bulle pour former la légende
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

    # On creer la courbe théorique
    plt.plot(x_array, y_array, '--')
    # On met le titre
    plt.title("Test du \u03C7\u00B2")
    # On met une legende sur l'axe y
    plt.ylabel('Frequence')
    plt.show()
    print(xhi2)


def get_xhi2_data(data):
    values = compute_reduced_centered_vars(data)
    min_value = values[0]
    max_value = values[-1]
    width = values[-1] - values[0]
    class_count = int(math.sqrt(len(values))) + 1
    class_width = width / class_count
    class_data = []
    integration_table = DataArray.load_array("Integrate_gauss")
    for i in range(class_count):
        class_ = ClassData()
        class_.infimum = min_value + class_width * i
        class_.supremum = (max_value + 1) if i == class_count - 1 else (min_value + (1 + i) * class_width)
        class_.population = population(min_value + class_width * i, min_value + (1 + i) * class_width, values)
        class_.experimental_frequency = class_.population / len(values)
        class_.theorical_frequency = theorical_frequency(class_.infimum, class_.supremum, integration_table)
        class_data.append(class_)
    xhi2 = class_count * sum(
        [(class_.experimental_frequency * class_.theorical_frequency) ** 2 / class_.theorical_frequency for class_ in
         class_data])
    return class_data, xhi2




__all__ = [
    "get_xhi2_data",
    "display_data"
]

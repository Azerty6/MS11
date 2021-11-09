import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
from DataArray import DataArray
from ClassData import ClassData
def ecart_centre_red(a, mean, ecart_type):
    b = (a - mean) / ecart_type
    return b


def population(a, b, data):
    pop = 0
    for value in data:
        if a <= value < b:
            pop += 1
    return pop


def theorical_frequency(a, b, integration_table):
    # int(a < 0) = -1 si a > 0, 1 si a < 0
    # Les calculs sont bizarres, mais ils doivent marcher ^^
    print(a)
    print(b)
    a = abs(int(100 * a))
    b = abs(int(100 * b))
    print((str(a // 100) + "." + str(a // 10 - a // 100 * 10), str(a - a // 10 * 10)))
    print((str(b // 100) + "." + str(b // 10 - b // 100 * 10), str(b - b // 10 * 10)))
    return \
        int(a < 0) * float(integration_table[str(a // 100) + "." + str(a // 10 - a // 100 * 10), str(a - a // 10 * 10)]) + \
        int(b > 0) * float(integration_table[str(b // 100) + "." + str(b // 10 - b // 100 * 10), str(b - b // 10 * 10)])


print("Sélectionnez votre échantillons de mesures (chaque mesure doit être séparée par une virgule)")
sample = sorted([int(i) for i in input("Echantillon:").split(",")])
sample_mean = statistics.mean(sample)

e_type_sb = statistics.stdev(sample, sample_mean)
values = sorted([ecart_centre_red(i, sample_mean, e_type_sb) for i in sample])

width = values[-1] - values[0]
class_count = int(math.sqrt(len(sample))) + 1
class_width = width / class_count
# Je pense que ça sert à rien, si on peut avoir plus précis, autant avoir plus précis
#class_width = round(class_width, 4) + 0.0001

# La même ici je pense
min_value = values[0] #round(values[0], 4) - 0.0001

# Format d'une class : [(borne_sup, borne_inf), population, fréquence_expérimentale, fréquence_théorique, x²]
class_data = []
for i in range(class_count):
    data = ClassData()
    data.infimum = min_value + class_width * i
    data.supremum = min_value + (1 + i) * class_width
    class_data.append(data)
# On ajoute 1 pour faire comme si l'intervalle était fermé. On aurait pu ajouter 2, 3, 4, 0.0000001,
# mais autant ajouter 1, c'est pratique ^^
#class_data[-1].supremum = values[-1] + 1
#J'ai pas compris ici, mais ça fesait un dernier intervalle incoherent


for i, data in enumerate(class_data):
    data.population = population(min_value + class_width * i, min_value + (1 + i) * class_width, values)
for data in class_data:
    data.experimental_frequency = data.population / len(values)

integration_table = DataArray.load_array("Integrate_gauss")
for data in class_data:
    data.theorical_frequency = theorical_frequency(data.infimum, data.supremum, integration_table)


xhi2 = class_count * sum(
    [(data.experimental_frequency * data.theorical_frequency) ** 2 / data.theorical_frequency for data in class_data])

bins_class = [] #On definis les diffférents intervalles
for data in class_data:
    bins_class.append(data.infimum)
bins_class.append(values[-1])

fig, ax = plt.subplots() #On cree la fenetre pyplot
exp_freq_array = np.array(values)#On change une liste en une matrice

print("Valeurs centrées réduites : " + str(values))
print("Etendue des valeurs : " + str(width))
print("Longueur des classes : " + str(class_width))
print("Données des classes : " + str(class_data))
print("xhi² : " + str(xhi2))
#10,10,11,11,11,13,12,9,12,14
#Echantillon test1
x = []
y = []
#On cree une liste d'antécendant une une matrice d'immage pour pouvoir
#creer la courbe théorique
while len(x) <= 100:
    x.append((sample[0]-sample_mean)+len(x)*(sample[-1]-sample[0])/100)
for i in range(len(x)):
    y.append((1 / (np.sqrt(2 * np.pi) * e_type_sb)) * np.exp(-0.5 * ((x[i]) / e_type_sb) ** 2))

num_bins = class_count
#On construit l'histogramme reel
n, bins, patches = ax.hist(exp_freq_array, num_bins, density=True)
#14,15,16,17,18,14,15,17,16,17,17,18,17,17,13,15,15,15,14,13,16,17,18,14,15,16,17,18,19,17,14,17,16,15,15,16
#echantillon test 2
#0.385,0.387,0.388,0.383,0.391,0.380,0.382,0.384,0,.386,0.389,0.390,0.385,0.389,0.388,0.382,0.387,0.388,0.392,0.383,0.388,0.385
#385,387,388,383,391,380,382,384,386,389,390,385,389,388,382,387,388,392,383,388,385
#On transforme les liste en matrice
x_array = np.array(x)
y_array = np.array(y)
#On met le teste de la bulle
textstr = "$\mu=%.2f${}\n$\sigma=%.2f${}\n\u03C7\u00B2={}".format(round(sample_mean, 3), round(e_type_sb, 3), round(xhi2, 4))
#On creer la bulle
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#On assemble le texte et la bulle pour former la légende
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#On creer la courbe théorique
plt.plot(x_array, y_array, '--')
#On met le titre
plt.title("Test du \u03C7\u00B2")
#On met une legende sur l'axe y
plt.ylabel('Frequence')


plt.show()


#print("La moyenne de l'echantillon est :", format(moy_sample))

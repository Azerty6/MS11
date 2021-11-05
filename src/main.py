import math
import statistics
from src.DataArray import DataArray
from src.ClassData import ClassData


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
class_data[-1].supremum = values[-1] + 1


for i, data in enumerate(class_data):
    data.population = population(min_value + class_width * i, min_value + (1 + i) * class_width, values)
for data in class_data:
    data.experimental_frequency = data.population / len(values)

integration_table = DataArray.load_array("Integrate_gauss")
for data in class_data:
    data.theorical_frequency = theorical_frequency(data.infimum, data.supremum, integration_table)


xhi2 = class_count * sum(
    [(data.experimental_frequency * data.theorical_frequency) ** 2 / data.theorical_frequency for data in class_data])

print("Valeurs centrées réduites : " + str(values))
print("Etendue des valeurs : " + str(width))
print("Longueur des classes : " + str(class_width))
print("Données des classes : " + str(class_data))
print("xhi² : " + str(xhi2))



#print("La moyenne de l'echantillon est :", format(moy_sample))

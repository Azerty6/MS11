import math
import statistics
import Integrale_theorique as Int

def ecart_centre_red(a, mean, ecart_type):
    b = 0
    b = (a - mean) / ecart_type
    return b

print("Selectionnerr votre echantillons de mesures")
sample_str = input("Echantillon:")
sample_str = sample_str.split(",")
sample_int = [int(i) for i in sample_str]
sample_sort = sorted(sample_int)
moy_sample = statistics.mean(sample_int)

e_type_sb = statistics.stdev(sample_int)
e_centre_red = []
for i in range(len(sample_sort)):
    e_centre_red.append(ecart_centre_red(sample_sort[i], moy_sample, e_type_sb))

largeur_tot = e_centre_red[-1]-e_centre_red[0]
nb_classes = int(math.sqrt(len(sample_int)))+1
largeur_classe = largeur_tot/nb_classes
largeur_classe = round(largeur_classe, 4)+0.0001

min_centre = round(e_centre_red[0], 4)-0.0001

tableau = []
for i in range(nb_classes):
    tableau.append(["[{};{} [".format(round(min_centre+largeur_classe*i, 4), round(min_centre+(1+i)*largeur_classe, 4))])

def population(a, b, liste):
    pop = 0
    for i in range(len(liste)):
        if liste[i] >= a and liste[i] <= b:
            pop = pop +1
        else:
            pop = pop
    return pop

def f_relative(pop, total):
    frequence_relative = pop/total
    frequence_relative = round(frequence_relative, 4)
    return frequence_relative
def f_theorique(a, b)

for i in range(nb_classes):
    tableau[i].append(population(round(min_centre+largeur_classe*i, 4), round(min_centre+(1+i)*largeur_classe, 4), e_centre_red))
for i in range(nb_classes):
    tableau[i].append(f_relative(tableau[i][1], len(e_centre_red)))
#for i in range(nb_classes):
#    tableau[i].append(f_theorique())
#for i in range(nb_classes):
#    tableau[i].append(f_xhi2)

print(e_centre_red)
print(largeur_tot)
print(largeur_classe)
print(tableau)



#print("La moyenne de l'echantillon est :", format(moy_sample))

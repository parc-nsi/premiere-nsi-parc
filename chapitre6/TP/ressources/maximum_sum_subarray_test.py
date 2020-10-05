from maximum_sum_subarray import *
from random import randint
from functools import wraps
import matplotlib.pyplot as plt
import numpy as np
import time


BSUP = 1000
BINF = -1000
TAILLEMAX = 1000
PAS = 50

def chrono(f):
    """Modifie le comportement de f,
    retourne un tuple (temps d'exécution, valeur retour de f)"""
    
    @wraps(f)
    def wraped(*args):
        debut = time.perf_counter()
        rep = f(*args)
        fin = time.perf_counter()
        return (fin - debut, rep)
    
    return wraped

def graphique():
    """Produit un graphique de comparaison de temps d'exécution des fonctions
    maximum_sum_subarray1 et maximum_sum_subarray2
    sur des tableaux de tailles croissantes"""
    #Construction des échantillons
    les_temps1 = []   #temps pour maximum_sum_subarray1 (complexlité cubique en O(n**3))
    les_temps2 = []   #temps pour maximum_sum_subarray2 (complexlité linéaire en O(n))
    maximum_sum_subarray1_chrono = chrono(maximum_sum_subarray1)
    maximum_sum_subarray2_chrono = chrono(maximum_sum_subarray2)
    les_tailles = np.arange(PAS, TAILLEMAX, PAS)
    for taille in les_tailles:
        tab = [randint(BINF, BSUP) for _ in range(taille)]
        (temps1, _)  = maximum_sum_subarray1_chrono(tab)
        (temps2, _)  = maximum_sum_subarray2_chrono(tab)
        les_temps1.append(temps1)
        les_temps2.append(temps2)

    #Conversion des listes d'échantillons en tableaux numpy
    les_temps1 = np.array(les_temps1)
    K1 = les_temps1[len(les_temps1) - 1] / les_tailles[len(les_tailles) - 1] ** 3
    les_temps2 = np.array(les_temps2)
    K2 = les_temps2[len(les_temps2) - 1] / les_tailles[len(les_tailles) - 1]
    #abscisses pour les courbes de fonctions
    les_x = np.linspace(0, TAILLEMAX, 1000)
    #Réalisation du graphique
    fig, ax = plt.subplots(3,1)
    fig.set_size_inches((10,10))
    ax[0].scatter(les_tailles, les_temps1 / K1)
    ax[0].plot(les_x, les_x ** 3,  label=r'$y=x^3$', color='red')
    ax[0].set_title("Temps d'exécution normalisée en secondes pour " + maximum_sum_subarray1_chrono.__name__)
    ax[0].set_ylabel("Temps en secondes")
    ax[0].legend()
    ax[0].set_xlabel("Taille du tableau")
    ax[1].scatter(les_tailles, les_temps2 / K2)
    ax[1].plot(les_x, les_x, label=r'$y=x$', color='red')
    ax[1].set_title("Temps d'exécution normalisée en secondes pour " + maximum_sum_subarray2_chrono.__name__)
    ax[1].set_ylabel("Temps en secondes")
    ax[1].legend()
    ax[1].set_xlabel("Taille du tableau")
    ax[2].scatter(les_tailles, (les_temps1  / K1)/ (les_temps2 / K2))
    ax[2].plot(les_x, les_x ** 2, label=r'$y=x^2$', color ='red')
    ax[2].set_title("Rapport des temps d'exécution normalisés")
    ax[2].set_xlabel("Taille du tableau")
    ax[2].legend()
    plt.subplots_adjust(hspace=1.5)
    fig.savefig("maximum-subarray-benchmark.png")

#Tests
BENCHMARK = [([-9, 5, -2, -1, -8, 7, 10, -1, 0, 1], 17),
             ([0, -4, 9, -2, 0, 10, 7, -1, 9, 9], 41),
             ([3, -9, -5, 4, 5, 5, -10, 9, -2, -8], 14),
             ([-7, -1, 6, 10, 1, 10, -2, -9, -2, -4], 27),
             ([3, 4, -7, 8, -6, 6, 2, -3, 0, -3], 10)]

for k, (tab, smax) in enumerate(BENCHMARK):
    assert maximum_sum_subarray1(tab) == smax, 'échec de maximum_sum_subarray1 sur le test {}'.format(k)
    assert maximum_sum_subarray2(tab) == smax, 'échec de maximum_sum_subarray1 sur le test {}'.format(k)
print('Tests unitaires réussis')
#Production du graphique
graphique()

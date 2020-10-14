##A copier dans partieB.py

import matplotlib.pyplot as plt

def diagramme(n, nbmax_essai):
    """Réalise un échantillon de nombres d'essais pour n parties
    Génère un diagramme batons et affiche la moyenne
    et la durée de création de l'échantillon
    """
    echantillon, duree = generer_echantillon(n, nbmax_essai)
    batons = [echantillon.count(k) for k in range(-1, nbmax_essai + 1)]
    plt.bar(list(range(-1, nbmax_essai + 1)), batons)
    plt.title("{} parties avec {} essais, en moyenne  {} essais max, Durée : {:.4} s".format(
        n, nbmax_essai, moyenne(echantillon), duree))
    plt.savefig("diagramme-{}.png".format(n))
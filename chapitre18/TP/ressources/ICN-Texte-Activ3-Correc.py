# -*- coding: utf-8 -*-

import re
from random import random
import matplotlib.pyplot as plt
import numpy as np



    

## Unigramme Top 50

    
def nettoyerFichier(fichier):
    f = open(fichier, 'r')
    data = f.read()
    data = re.sub(r'[^\w\s]', ' ', data)
    data = re.sub(r'\s+',' ', data)
    f.close()
    return data.lower()
    
            
def listmot(source):
    texte = nettoyerFichier(source)
    return texte.split(' ')
    
def histogramme(L):
    histo = {}
    for mot in L:
        if mot != '':
            if mot not in histo:
                histo[mot] = 1
            else:
                histo[mot] += 1
    return histo
    
def topUnigramme(source, but):
    lesmots = listmot(source)
    histo = histogramme(lesmots)
    classement = sorted(list(histo.items()), key = lambda t : t[1], reverse = True)
    g = open(but, 'w')
    for mot, effectif in classement:
        g.write(mot + ' ' + str(effectif) + '\n')
    g.close()
    return classement

def graphiqueUnigramme(source):
    lesmots = listmot(source)
    histo = histogramme(lesmots)
    classement = sorted(list(histo.items()), key = lambda t : t[1], reverse = True)
    racine, ext = source.split('.')
    g = open(racine + '-unigramme' + '.' +  ext, 'w')
    for mot, effectif in classement:
        g.write(mot + ' ' + str(effectif) + '\n')
    g.close()
    top50 = classement[:50]
    mot50 = [element[0] for element in top50]
    score50 = [element[1] for element in top50]
    plt.xticks(range(1, 51), mot50, rotation=60)
    plt.xlabel('Mots')
    plt.ylabel('Nombre d\'occurences')
    plt.title('Top 50 des mots les plus fréquents dans {:}'.format(racine))
    plt.bar(range(1, 51), score50)
    plt.savefig('top50-' + racine + '.png')
    plt.show()
    
    
## Digrammes

def prochainHisto(source):
    '''Retourne un dictionnaire de dictionnaires  avec pour chaque mot un 
    histogramme des mots suivants'''
    lesmots = listmot(source)
    nbmot = len(lesmots)
    prochain = dict()
    for k in range(nbmot - 1):
        mot = lesmots[k]
        suivant = lesmots[k + 1]
        if mot != '':
            if mot not in prochain:
                prochain[mot] = dict()
                prochain[mot][suivant] = 1
            else:
                if suivant not in prochain[mot]:
                    prochain[mot][suivant] = 1
                else:
                    prochain[mot][suivant] += 1
    return prochain

def sommeHisto(histo):
    '''Retourne la somme des effectifs d'un histogramme
    sous forme de dictionnaire'''
    s = 0
    for clef, effectif in histo.items():
        s = s + effectif
    return s
    
def prochainFreq(source):
    prochain = prochainHisto(source)
    freq = dict()
    for mot in prochain:
        freq[mot] = dict()
        histo = prochain[mot]
        nbsuivant = sommeHisto(histo)
        for suivant, effectif in histo.items():
            freq[mot][suivant]= effectif / nbsuivant
    racine, ext = source.split('.')
    fichierFreq = racine + '-freq-digrammes' +  ext
    g = open(fichierFreq, 'w')
    for mot in freq:
        for suivant, f in sorted(list(freq[mot].items()), key = lambda t : t[1], reverse = True):
            g.write(mot + ' ' + suivant + ' ' + str(f) + '\n')
    g.close()
    return freq
    
## Génération de texte par chaine de Markov

def histoCumul(histo):
    """Liste de couples (clef, frequence cumuléé) à partir du dictionnaire
    histo de fréquences """
    histo = [(mot, effectif) for mot, effectif in histo.items()]
    histoC = [histo[0]]
    for k in range(1, len(histo)):
        histoC.append((histo[k][0],  histoC[-1][1] + histo[k][1]))
    return histoC
    
def motSuivant(mot, freq):
    histoC = histoCumul(freq[mot])
    alea = random()
    k = 0
    while histoC[k][1] <= alea:
        k += 1
    return histoC[k][0]
    
"""Vérification
In [18]: freq['pose']
Out[18]: {'et': 0.25, 'gracieuse': 0.25, 'qui': 0.5}

In [19]: mot = 'pose'

In [20]: dist = freq[mot]

In [21]: echantillon = [motSuivant(mot, freq) for k in range(5000)]

In [22]: [echantillon.count(suivant)/5000 for suivant in dist]
Out[22]: [0.5044, 0.249, 0.2466]

In [23]: [(suivant, echantillon.count(suivant)/5000) for suivant in dist]
Out[23]: [('qui', 0.5044), ('et', 0.249), ('gracieuse', 0.2466)]
"""

def autoTexte(source, debut, taille):
    freq = prochainFreq(source)
    racine, ext = source.split('.')
    sortie = racine + '-auto-' + '.' + ext
    f = open(sortie, 'w')
    mot = debut
    f.write(mot + ' ')
    nbmotligne = 0
    for k in range(taille - 1):
        suivant = motSuivant(mot, freq)
        mot = suivant
        f.write(mot + ' ')
        nbmotligne = nbmotligne + len(suivant)
        if nbmotligne >= 20:
            f.write('\n')
            nbmotligne = 0
    f.close()
    
    
    
    
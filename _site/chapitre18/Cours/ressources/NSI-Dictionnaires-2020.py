#!/usr/bin/env python
# coding: utf-8

# ## Test de performances de l'opérateur in 
# 
# 
# * Source : Python Fluent Chapitre 1 Dict and Set <https://github.com/fluentpython/example-code-2e/tree/master/03-dict-set/support>

# ## container_perftest.py

# In[21]:


"""
Container ``in`` operator performance test

Auteur : Luciano Ramalho "Fluent Python"
Source : https://github.com/fluentpython/example-code-2e/tree/master/03-dict-set/support
"""
import sys
import timeit

#Initialisation d'un test 
#avec les valeurs des tableaux haystack pour la meule de foin (zone de recherche)
#et needles (auiguilles/clefs recherchées dans haystack)
SETUP = '''
#import du module permettant de créer des tableaux homogènes
import array  
#création d'un tableau de flottants
selected = array.array('d')
#on sélectionne size flottants dans le fichier selected.arr
#size = 10**k avec 3 <= k <= 7
with open('selected.arr', 'rb') as fp:
    selected.fromfile(fp, {size})
#création de la meule de foin haystack
#1ercas : si le conteneur testé est de type dict
if {container_type} is dict:
    haystack = dict.fromkeys(selected, 1)
#2eme cas : list ou set
else:
    haystack = {container_type}(selected)
#en mode verbeux (verbose est un booléen on affiche une trace de chaque recherche)
if {verbose}:
    print(type(haystack), end='  ')
    print('haystack: %10d' % len(haystack), end='  ')
#on crée le tableau des aiguilles
needles = array.array('d')
#on sélectionne 500 aiguilles dans not_selected.arr 
#on est sur qu'elles ne sont pas dans selected.arr et donc pas dans haystack
with open('not_selected.arr', 'rb') as fp:
    needles.fromfile(fp, 500)
#on complète needles avec 500 aiguilles dans selected.arr et donc dans haystack
needles.extend(selected[::{size}//500])
if {verbose}:
    print(' needles: %10d' % len(needles), end='  ')
'''

#Initialisation du code testé
TEST = '''
found = 0
for n in needles:
    if n in haystack:
        found += 1
if {verbose}:
    print('  found: %10d' % found)
'''

def test(container_type, verbose):
    """Test la performance de l'opérateur in pour le conteneur 
    de type container_type"""
    print("Type de conteneur {}".format(container_type))
    print('-'* 20)
    MAX_EXPONENT = 7
    #boucle sur la taille de la meule de foin haystask entre 10**3 et 10**7
    for n in range(3, MAX_EXPONENT + 1):
        #initialisation de la taille de la meule de foin haystack
        size = 10**n
        #on paramètre l'initialisation des variables haystack et needles
        setup = SETUP.format(container_type=container_type,
                             size=size, verbose=verbose)
        #on paramètre le test (affichage verbeux ou pas)
        test = TEST.format(verbose=verbose)
        #on répète 5 fois le code test avec les variables initialisées dans setup
        tt = timeit.repeat(stmt=test, setup=setup, repeat=5, number=1)
        if verbose:
            print("Temps d'exécution des 5 boucles ", tt)
        print('Taille de la meule de foin : {:{}d}'.format(size, MAX_EXPONENT + 1))
        print('Temps minimum de recherche de 1000 aiguilles  (sur 5 recherches): {:f} s'.format(min(tt)))
        print('-'* 20)

#le code peut être exécuté depuis la ligne de commandes :
"""
Pour un test avec un dictionnaire (type dic) :
>>> python3 dict
Pour u ntest avec une liste python (type list) :
>>> python3 list
"""

if __name__=='__main__':
    #l'option facultative -v délcenche le mode verbeux 
    #elle peut être avant ou après l'option de type  de conteneur obligatoire
    if '-v' in sys.argv:        
        sys.argv.remove('-v')
        verbose = True
    else:
        verbose = False
    if len(sys.argv) != 2:
        print('Usage: %s <container_type>' % sys.argv[0])
    else:
        test(sys.argv[1], verbose)


# ## container_perftest_datagen.py

# In[24]:


"""
Generate data for container performance test

Auteur : Luciano Ramalho "Fluent Python"
Source : https://github.com/fluentpython/example-code-2e/tree/master/03-dict-set/support
"""

import random
import array

#varaibles globales
MAX_EXPONENT = 7
HAYSTACK_LEN = 10 ** MAX_EXPONENT
NEEDLES_LEN = 10 ** (MAX_EXPONENT - 1)
SAMPLE_LEN = HAYSTACK_LEN + NEEDLES_LEN // 2


#ensemble de SAMPLE_LEN  flottants double précision
sample = {1/random.random() for i in range(SAMPLE_LEN)}
print('initial sample: %d elements' % len(sample))

#un ensemble n'a pas de doublons
#on complète l'ensemble jusqu'à obtenir une taille de SAMPLE_LEN 
#tant qu'il y a des doublons
# SAMPLE_LEN correspond
while len(sample) < SAMPLE_LEN:
    sample.add(1/random.random())

print('complete sample: %d elements' % len(sample))

#création d'un tableau de flottants double précision 
#à partir de l'échantillon sans doublons sample
#au passage sample passe du type set au type array (typage dynamique en Python)
sample = array.array('d', sample)
#mélange de sample
random.shuffle(sample)

#on sélectionne NEEDLES_LEN // 2 (égal à 500 000) flottants dans sample
not_selected = sample[:NEEDLES_LEN // 2]
print('not selected: %d samples' % len(not_selected))
print('  writing not_selected.arr')
#on les enregistre dans le  fichier binaire not_selected.arr
#de taille 500 000 * 8 = 4 000 0000 octets
#avantage du type array : les flottants double précision sont codés sur 8 octets comme en C
with open('not_selected.arr', 'wb') as fp:
    not_selected.tofile(fp)

#on sélectionne  les autres flottants de sample (soit 10 000 000)
selected = sample[NEEDLES_LEN // 2:]
print('selected: %d samples' % len(selected))
print('  writing selected.arr')
#on les enregistre dans le  fichier binaire selected.arr
with open('selected.arr', 'wb') as fp:
    selected.tofile(fp)


# ## Test pour un dictionnaire

# In[25]:


test('dict', False)


# In[23]:


test('list', False)


# ## Des p-uplets aux p-uplets nommés

# In[50]:


import csv

def fichier_vers_tab(fichier, separateur):
    """Prend en paramètres :
    - fichier de type str représentant un chemin d'accès à un fichier texte
    - separateur de type str désignant le séparateur de champs sur une ligne du fichier
    Retourne un tuple de 2  tableaux :
    - un tableau de tuples
    - un tableau de tuples nommés (dictionnaires)
    """
    #on ouvre le fichier 2 fois en lecture
    f = open(fichier)
    g = open(fichier)
    csv_reader = csv.DictReader(f, delimiter=separateur)
    tab_dico = [ligne for ligne in csv_reader]
    #saut de la ligne d'en-tete
    g.readline()
    tab_tuple = [tuple(ligne.strip().split(separateur)) for ligne in g]
    #on ferme les fichiers
    g.close()
    f.close()
    return (tab_tuple, tab_dico)


# In[51]:


(tab_tuple_airports, tab_dico_airports) = fichier_vers_tab('airports-reduit-avec-entete.csv', ';')


# In[52]:


tab_dico_airports[32478]


# In[54]:


tab_tuple_airports[32478]


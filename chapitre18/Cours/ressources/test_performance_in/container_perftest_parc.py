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

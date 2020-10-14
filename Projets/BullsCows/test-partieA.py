from partieA import *

## Test de combinaison_secrete
def test_combinaison_secrete(nbtest):
    for _ in range(nbtest):
        for c in combinaison_secrete():
            assert isinstance(c, int) and 0 <= c <= 9
    print('Tests réussis pour combinaison_secrete')
    

##Décommentez pour le test :
#test_combinaison_secrete(10000)

## Test de nombre_bien_places


def test_nombre_bien_places():
    for i in range(10):
        for j in range(10):
            assert nombre_bien_places([i,1,1,1], [j,2,2,2]) == (1 if i == j else 0)
            assert nombre_bien_places([1,i,1,1], [2,j,2,2]) == (1 if i == j else 0)
            assert nombre_bien_places([1,1,1,i], [2,2,2,j]) == (1 if i == j else 0)
            assert nombre_bien_places([1,i,i,1], [2,j,j,2]) == (2 if i == j else 0)
            assert nombre_bien_places([i,i,i,i], [j,j,j,j]) == (4 if i == j else 0)
    print('Tests réussis pour nombre_bien_places')
         

##Décommentez pour le test :
#test_nombre_bien_places()


##Test de minimum
import random

def test_minimum():
    for _ in range(1000):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        assert minimum(a, b) == min(a,b)
    print('Tests réussis pour minimum')

##Décommentez pour le test :
#test_minimum()

## Test de histo


def test_histo():
    assert histo([3,6,3,1]) == [0,1,0,2,0,0,1,0,0,0]
    #à compléter avec des assert
    print('Tests réussis pour histo')
         

##Décommentez pour le test :
#test_histo()


## Test de nombre_communs


def test_nombre_communs():
    assert nombre_communs([5,5,5,5], [5,5,5,5]) == 4
    assert nombre_communs([4,4,4,4], [3,3,3,3]) == 0
    assert nombre_communs([4,6,4,1], [4,4,4,6]) == 3
    #à compléter avec des assert
    print('Tests réussis pour nombre_communs')
         

##Décommentez pour le test :
#test_nombre_communs()


##Test de nombre_bulls_cows

def test_nombre_bulls_cows():
    assert nombre_bulls_cows([5,5,5,5], [5,5,5,5]) == [4,0]
    assert nombre_bulls_cows([4,4,4,4], [3,3,3,3]) == [0,0]
    assert nombre_bulls_cows([4,2,4,2], [2,4,2,4]) == [0,4]
    #à compléter avec des assert
    print('Tests réussis pour nombre_bulls_cows')

##Décommentez pour le test :
#test_nombre_bulls_cows()

